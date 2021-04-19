from PyDictionary import PyDictionary

import RelevantSentences.GetText as GetTextFile
import Data.SearchResult as SearchResultFile

from nltk.tokenize import word_tokenize


class Index(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.index = PyDictionary()


class Book:
    def __init__(self):
        self.title = None
        self.file_type = None
        self.contents = None
        self.pages_list = None
        self.lines = None
        self.index = None

    def searchForWords(self, searchQuery):
        print("Searching for...", searchQuery)
        for i in self.index:
            print("item in index->", i)

        print("Searching for... found->", self.index)
        return self.index.synonym_find(searchQuery)

    def setBook(self, file):
        print("Path", file)

        if self.file_type == ".txt":
            print("We are working with a .txt file")
            # self.contents = file.read()
            self.contents = file.read()
            print("self.contents ", self.contents)

            self.index = self.create_index_txt()

            print("index->", self.index)
            print("Contents->", self.contents)

        else:
            print("Filetype Error")

    def create_index_txt(self):
        print("creating index")

        index = Index()

        print('contents: ', self.contents)

        contentsCleaned = word_tokenize(self.contents.lower())

        for i, word in enumerate(contentsCleaned):
            if not word.isalpha():
                continue

            if word not in index:
                index[word] = list()

            newRes = SearchResultFile.SearchResult()
            newRes.word = word
            newRes.position = i

            index[word].append(newRes)

        return index







