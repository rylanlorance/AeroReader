class SupervisedMainView(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.mainVBox = QVBoxLayout()
        self.setLayout(self.mainVBox)

        # self.formGroupBox = QGroupBox(title="MyGroupBox")
        # self.formGroupBox_height = 200
        # self.formGroupBox_width = 200
        # self.formGroupBox.setGeometry(QtCore.QRect(0, 0, self.formGroupBox_width, self.formGroupBox_height))
        # self.fbox = QFormLayout()
        # self.fbox.setAlignment(Qt.AlignLeft)
        # self.fbox.setGeometry(QtCore.QRect(0, 0, self.formGroupBox_height, self.formGroupBox_width))

        self.__createFormBox()
        self.mainVBox.addWidget(self.formGroupBox)


        # self.mainVBox.addSpacing(150)

        # self.itemRowBox = SupervisedSearchItemRow(self, "SearchWord")
        # self.mainVBox.addWidget(self.itemRowBox)

    def __createFormBox(self):

        self.l1 = QLabel("Search here")

        self.searchBar = QLineEdit()
        self.l1.setAlignment(Qt.AlignLeft)
        self.l1.setAlignment(Qt.AlignBottom)

        self.fbox.addRow(self.l1, self.searchBar)

        self.searchButton = QPushButton("Search")
        self.searchButton.clicked.connect(self.__searchButtonClicked)
        self.fbox.addRow(self.searchButton)

        self.formGroupBox.setLayout(self.fbox)

        # hardcoded, change this later.
        # self.__loadSearchResults("SearchString")

    def __searchButtonClicked(self):
        searchString = self.searchBar.text()
        print("Working with the following : [{0}]".format(searchString))
        searchString.lower()

    def __loadSearchResults(self, searchString):
        # try this
        sr1 = SearchResult()
        sr2 = SearchResult()
        print("Loading Search Screen")
