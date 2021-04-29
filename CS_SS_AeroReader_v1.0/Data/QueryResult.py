class QueryResult:
    def __init__(self):
        self.query = None
        self.queryLocations = None  # actual query item itself (i.e. user searches for spider-> list of locations of spider)
        self.synonymLocations = list()
