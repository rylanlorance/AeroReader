from collections import namedtuple
from typing import Callable, List, Dict, Union

import fitz  # pymupdf package
from PyDictionary import PyDictionary
from nltk.tokenize import word_tokenize

# Record that keeps page number and index of the word on the page
word_record = namedtuple('word_record', ('page', 'word_index'))


# SynonymDict subclasses dict to create a function that finds and returns all synonym entries
# of a word (including the word itself)

class SynonymDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._thesaurus = PyDictionary()

    def synonym_find(self, word: str) -> Dict[str, List[str]]:
        synonyms = [synonym.lower() for synonym in self._thesaurus.synonym(word)]

        for synonym in synonyms:
            s = synonym.split(' ')

            if len(s) > 1:
                synonyms.append(s[-1])

        locations = {synonym: self[synonym] for synonym in synonyms if synonym in self}

        if word in self:
            locations[word] = self[word]

        return locations


def clean_words(words: str) -> str:
    return word_tokenize(words.lower())


def extract_all(file: str, clean_function: Callable[[str], Union[str, List[str]]],
                word_break: int = 300) -> List[str]:
    """
        Extracts text from a txt, runs cleaning function on each page of text

        :param file: Book's PDF file path
        :param clean_function: cleans text in desired way for each page
        :param word_break: amount of words to include in each page
        :return: Pages list where each index i corresponds to page i
    """

    with open(file) as book:
        words = clean_function(book.read())

    n = len(words)

    pages = [words[i:i+word_break] for i in range(0, n, word_break)]

    return pages

def count_instances(pages: List[str]) -> SynonymDict:
    """
    :param pages: A list where each index i corresponds to page i's contents
    :return: Returns a synonym dictionary cataloguing every word's locations within the text
    """
    words = SynonymDict()

    for i, page in enumerate(pages):
        for j, word in enumerate(page):
            if not word.isalpha():
                continue

            if word not in words:
                words[word] = list()

            words[word].append(word_record(i, j))

    return words
