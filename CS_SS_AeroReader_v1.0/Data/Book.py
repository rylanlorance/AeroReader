import RelevantSentences.GetText as GetTextFile


class Book:
    def __init__(self):
        self.title = None
        self.file_type = None
        self.contents = None
        self.pages_list = None
        self.index = None

    def setPages(self, file):
        print("Path", file)

        if self.file_type == ".txt":
            print("We are working with a .txt file")
            self.pages_list = [file.read()]

            self.contents = file.read()

            self.index = GetTextFile.count_instances(self.pages_list)
            print("index->", self.index)

        elif self.file_type == ".pdf":
            print("We are working with a .pdf file")

        else:
            print("Filetype Error")



