from PyDictionary import PyDictionary

import RelevantSentences.GetText as GetTextFile
import Data.QueryResult as QueryResultFile

import Data.SearchResultItem as SearchResultFile

from nltk.tokenize import word_tokenize



class Index(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.index = PyDictionary()


class Book:
    def __init__(self, nn):
        self.neural_net = nn
        self.clusters = None

        self.title = None
        self.file_type = None
        self.file = None
        self.contents = None
        self.pages_list = None
        self.lines = None
        self.index = None

    def searchForWords(self, searchQuery):
        print("Searching for...", searchQuery)
        searchQueryFormatted = searchQuery.lower()

        res = QueryResultFile.QueryResult()
        res.query = searchQueryFormatted

        if searchQuery in self.index:
            res.queryLocations = self.index[searchQueryFormatted]
        print("Res.queryLocations", res.queryLocations)

        try:
            synResult = self.neural_net.search(searchQueryFormatted, clusters=self.clusters)
        except Exception as e:
            synResult = []
            print(f"neural net search error: {e}")

        for result in synResult:
            print("Result", result)

            if result[0] in self.index:
                res.synonymLocations.append(self.index[result[0]])

        return res


    def setBook(self, file):
        # print("Path", file)

        if self.file_type == ".txt":
            # print("We are working with a .txt file")

            self.file = file

            self.contents = file.read()
            file.close()

            # print("self.contents ", self.contents)

            self.index = self.create_index_txt()

        else:
            print("Filetype Error")

    def create_index_txt(self):
        print("creating index")

        index = Index()
        self.lines = list()

        with open(self.file.name) as file:
            for i, line in enumerate(file):
                self.lines.append(line)

                for j, word in enumerate(word_tokenize(line.lower())):
                    if not word.isalpha():
                        continue

                    if word not in index:
                        index[word] = list()

                    newRes = SearchResultFile.SearchResultItem()
                    newRes.word = word
                    newRes.line_pos = i
                    newRes.word_pos = j

                    index[word].append(newRes)

        return index







