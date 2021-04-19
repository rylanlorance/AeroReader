import RelevantSentences.GetText as GetTextFile


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
            text = file.read()
            print("Text: ", text)


            # for line in self.lines:
            #     print("line: ", line)
            #     list = line.strip()
            #     print(list)

            # self.index = GetTextFile.count_instances(self.pages_list)
            print("pages", self.pages_list)
            print("index->", self.index)
            print("Contents->", self.contents)

        else:
            print("Filetype Error")
