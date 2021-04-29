from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRect
from PyQt5 import QtCore
from PyQt5.QtGui import *

import sys

from Data.SearchResultItem import SearchResultItem
from View.SupervisedSearchItemRow import SupervisedSearchItemRow
from Data.QueryResult import QueryResult


class SupervisedMainView(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.mainVBox = QVBoxLayout()
        self.setLayout(self.mainVBox)
        self.parent = parent
        self.showResponseUI = True

        self.queryResult = QueryResult()
        self.queryResult.query = ""

        self.localBook = self.parent.getBook()

        self.formBoxGroup = QGroupBox("")

        self.__createSeachBox()

        self.mainVBox.addWidget(self.formBoxGroup)

        # self.searchItemRow = SupervisedSearchItemRow(parent, "mySearchString")
        # self.mainVBox.addWidget(self.searchItemRow)

        self.searchListArea = QScrollArea()

        self.queryFormBoxLayout = QVBoxLayout()

        self.queryLayout = QVBoxLayout()
        self.queryWidget = QWidget()

        self.queryFormBox = QGroupBox("Results for [Search Result]")
        self.queryFormBox.setMaximumHeight(250)
        self.querySynFormBox = QGroupBox("Results for words similar to [Search Result]")
        self.querySynFormBox.setMaximumHeight(250)

        self.createSearchResponseArea()

    def init(self):
        self.localBook = self.parent.getBook()
        self.createSearchResponseArea()

    def createSearchResponseArea(self):
        print("Query Result->", self.queryResult.query)

        if self.showResponseUI and self.queryResult.query != "":
            self.queryWidget.setLayout(self.queryLayout)
            self.queryWidget.setStyleSheet("background-color: rgb(205, 237, 190)")

            self.queryFormBox.setTitle("Results for {}".format(self.queryResult.query))
            self.createQueryResultBox()

            self.querySynFormBox.setTitle("Results for Words Similar to {}".format(self.queryResult.query))
            self.createSynResultBox()

            self.queryLayout.addWidget(self.queryFormBox)
            self.queryLayout.addWidget(self.querySynFormBox)

            self.mainVBox.addWidget(self.queryWidget)

        else:
            print("Search Error")

    def createSynResultBox(self):
        self.synFormBoxLayout = QVBoxLayout()
        self.querySynFormBox.setLayout(self.synFormBoxLayout)

        # clear the layout
        for i in reversed(range(self.synFormBoxLayout.count())):
            self.synFormBoxLayout.itemAt(i).widget().setParent(None)

        if self.queryResult.synonymLocations is None or len(self.queryResult.synonymLocations) == 0:
            print("We could not find any words similar to ", self.queryResult.query)
            errorText = "No words found similar to {0}".format(self.queryResult.query)
            errorLabel = QLabel(errorText)
            self.synFormBoxLayout.addWidget(errorLabel)

        else:
            self.synScrollArea = QScrollArea()
            self.synScrollArea.setWidgetResizable(True)

            widget = QWidget()
            self.synScrollArea.setWidget(widget)
            synScrollLayout = QVBoxLayout(widget)

            for similarWord in self.queryResult.synonymLocations:
                print("similar word->", similarWord)
                for similarWordLocation in similarWord:
                    lineContext = self.localBook.lines[similarWordLocation.line_pos]
                    row = SupervisedSearchItemRow(self, similarWordLocation, lineContext)
                    synScrollLayout.addWidget(row)

            self.synFormBoxLayout.addWidget(self.synScrollArea)

    def createQueryResultBox(self):

        self.queryFormBox.setLayout(self.queryFormBoxLayout)

        for i in reversed(range(self.queryFormBoxLayout.count())):
            self.queryFormBoxLayout.itemAt(i).widget().setParent(None)

        if self.queryResult.queryLocations is None or len(self.queryResult.queryLocations) == 0:
            print("We dont have this word")
            errorText = "No results found"
            errorLabel = QLabel(errorText)
            self.queryFormBoxLayout.addWidget(errorLabel)

        else:
            self.queryScrollArea = QScrollArea()
            self.queryScrollArea.setWidgetResizable(True)

            widget = QWidget()
            self.queryScrollArea.setWidget(widget)
            scrollLayout = QVBoxLayout(widget)

            for searchResItem in self.queryResult.queryLocations:
                lineContext = self.localBook.lines[searchResItem.line_pos]
                row = SupervisedSearchItemRow(self, searchResItem, lineContext)
                scrollLayout.addWidget(row)

            self.queryFormBoxLayout.addWidget(self.queryScrollArea)

    def __createSeachBox(self):
        self.fboxLayout = QFormLayout()
        self.nm = QLineEdit()
        btn = QPushButton("Search")
        self.fboxLayout.addRow(self.nm, btn)

        btn.clicked.connect(self.__searchButtonClicked)

        self.formBoxGroup.setLayout(self.fboxLayout)

    def __searchButtonClicked(self):
        searchString = self.nm.text()

        if self.localBook.index is None:
            print("Warning... error")

        else:
            self.queryResult = self.localBook.searchForWords(searchString)
            self.init()



