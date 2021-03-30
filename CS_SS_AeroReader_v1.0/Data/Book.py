import RelevantSentences.GetText as GetTextFile
class Book:
    def __init__(self):
        self.title = None
        self.file_type = None
        self.contents = None
        self.pages_list = None

    def __setPagesList(self, path):
        print("Path", path)
        pages_list = GetTextFile.extract_all(path)
        print("Pages_list", pages_list)