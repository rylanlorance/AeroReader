import RelevantSentences.GetText as GetTextFile


class Book:
    def __init__(self):
        self.title = None
        self.file_type = None
        self.contents = None
        self.pages_list = None
        self.index = None

    def searchForWords(self, searchQuery):
        print("Searching for...", searchQuery)
        for i in self.index:
            print("item in index->", i)


        print("Searching for... found->", self.index)
        return self.index.synonym_find(searchQuery)



    def setPages(self, file):
        print("Path", file)

        if self.file_type == ".txt":
            print("We are working with a .txt file")
            self.pages_list = [file.read()]

            self.contents = self.pages_list[0]

            self.index = GetTextFile.count_instances(self.pages_list)
            print("pages", self.pages_list)
            print("index->", self.index)
            print("Contents->", self.contents)

        elif self.file_type == ".pdf":
            print("We are working with a .pdf file")

        else:
            print("Filetype Error")



