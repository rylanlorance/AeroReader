from abc import ABC
from argparse import ArgumentParser
from dataclasses import dataclass
from inspect import signature
from string import punctuation
from typing import List

import numpy as np
import scipy.sparse as sparse

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.cluster import AgglomerativeClustering

import Unsupervised.GetText as GetText

class BaseInterface(ABC):
    def __repr__(self):
        parameters = \
            ', '.join(f'{param}={getattr(self, param)}' for param in signature(self.__init__).parameters)

        return f'{self.__class__.__name__}({parameters})'

class CleanText(BaseInterface):
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.ignore = set(stopwords.words('english'))

        # Dictionary to remove punctuation
        self.remove_punctuation = str.maketrans('\n', ' ', punctuation)

        # Seen set for vector indexing
        self.seen = set()

    def __call__(self, text: str) -> List[str]:
        """
        :param text: String to stem and remove stop words from
        :return: Returns a list of relevant filtered words
        """

        words = word_tokenize(text.lower().translate(self.remove_punctuation))
        words = [self.lemmatizer.lemmatize(word) for word in words
                 if word not in self.ignore and word.isalpha()]

        self.seen.update(words)

        return words

class TextCluster(BaseInterface):
    @dataclass
    class Cluster(BaseInterface):
        example_page: str
        page_numbers: List[int]
        frequent_words: List[str]

    def __init__(self, book: str, n_clusters: int = 15):
        """
        :param book: file path to book pdf
        :param n_clusters: number of clusters to find within text
        """

        self.clusters, self.sentences = None, None
        self.book, self.n_clusters = book, n_clusters

        # Process each page as its own entry
        cleaner = CleanText()

        self.raw_pages = GetText.extract_all(book, lambda text: text)

        pages = [cleaner(page) for page in self.raw_pages]

        # Record word order for making word vectors
        words = np.array(list(cleaner.seen))
        words.sort()

        self.words = words

        self.used = np.array([i for i, page in enumerate(pages) if page])

        unused = [i for i, page in enumerate(pages) if not page]
        n = len(unused)

        self.counts = np.zeros((len(self.used), words.size), dtype='int32')

        # Create vectors for each sentence
        j = 0
        for i, page in enumerate(pages):
            if j < n and i == unused[j]:
                j += 1
                continue

            idx = words.searchsorted(page, 'left')
            numbers, count = np.unique(idx, return_counts=True)

            self.counts[i - j, numbers] = count

        self.tree = AgglomerativeClustering(n_clusters=self.n_clusters, affinity='cosine', linkage='complete')
        self.tree.fit(self.counts)

    def closest_pages(self, centroids) -> np.ndarray:
        """
        :param: representatives of each cluster
        :return: The most emblematic example page for each cluster
        """

        labels = self.tree.labels_

        _, counts = np.unique(labels, return_counts=True)

        np.true_divide(centroids, counts[:, np.newaxis], out=centroids)

        norms = np.linalg.norm(centroids, axis=1, keepdims=True)

        unit_ball = np.true_divide(
            centroids, norms, out=centroids
        )

        W = sparse.csr_matrix(self.counts)
        W = W / np.sqrt(W.power(2).sum(axis=1))

        angles = W @ unit_ball.T
        angles = np.subtract(angles, 1, out=angles)
        return np.abs(angles, out=angles)

    def tree_analysis(self):
        """
            Creates TextCluster.cluster instances for each passed cluster
        """

        # Initialize empty cluster objects to store relevant information
        self.clusters = [TextCluster.Cluster('', [], []) for _ in range(self.n_clusters)]

        labels = self.tree.labels_

        cluster_counts = np.zeros(
            (self.n_clusters, self.counts.shape[1]), dtype=np.float64
        )

        # Add up all word instances in a given cluster
        np.add.at(cluster_counts, labels, self.counts)

        # Gives indices of most frequently occurring words in a cluster
        top_words = cluster_counts.argsort(axis=1)

        # Attach words to each cluster
        for i, row in enumerate(top_words[:, -1:-10:-1]):
            self.clusters[i].frequent_words.extend(
                self.words[row]
            )

        # Getting similarity scores across each page for each cluster
        scores = self.closest_pages(cluster_counts).T
        scores = scores.argsort(axis=1)

        # Attach page numbers of 10 most emblematic pages in cluster
        # Attach emblematic page text
        n = len(self.used)
        for i, row in enumerate(scores[:, ::-1]):
            j = 0
            while j < n and self.tree.labels_[row[0, j]] != i:
                j += 1

            self.clusters[i].page_numbers.append(self.used[row[0, j]])
            self.clusters[i].example_page = self.raw_pages[self.used[row[0, j]]]

            while j < n and len(self.clusters[i].page_numbers) < 10:
                if self.tree.labels_[row[0, j]] == i:
                    self.clusters[i].page_numbers.append(self.used[j])

                j += 1

        return self.clusters

if __name__ == '__main__':
    args = ArgumentParser()
    args.add_argument('document', help='document to be used for analysis')
    args = args.parse_args()

    Tree = TextCluster(args.document)
