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

        self.formBoxGroup = QGroupBox("Search Group")

        self.__createSeachBox()

        self.mainVBox.addWidget(self.formBoxGroup)

        # self.searchItemRow = SupervisedSearchItemRow(parent, "mySearchString")
        # self.mainVBox.addWidget(self.searchItemRow)

        self.searchListArea = QScrollArea()

        self.queryLayout = QVBoxLayout()
        self.queryWidget = QWidget()

        self.queryFormBox = QGroupBox("Results for [Search Result]")
        self.querySynFormBox = QGroupBox("Results for words similar to [Search Result]")

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

            self.querySynFormBox.setTitle("Results for Synonyms of {}".format(self.queryResult.query))
            self.createSynResultBox()

            self.queryLayout.addWidget(self.queryFormBox)
            self.queryLayout.addWidget(self.querySynFormBox)

            self.mainVBox.addWidget(self.queryWidget)

        else:
            print("Search Error")

    def createSynResultBox(self):
        self.synFormBoxLayout = QVBoxLayout()

    def createQueryResultBox(self):
        self.queryFormBoxLayout = QVBoxLayout()
        self.queryFormBox.setLayout(self.queryFormBoxLayout)

        resultRow = SupervisedSearchItemRow(self)
        self.queryFormBoxLayout.addWidget(resultRow)

        for loc in self.queryResult.queryLocations:
            print("Query location obj = ", loc)
            print("Query location obj info = ", loc.word)
            print("Query location obj pos = ", loc.position)
            print("Word grab in txt ", self.localBook.contents[loc.position])


    def __createSeachBox(self):
        self.fboxLayout = QFormLayout()
        self.l1 = QLabel("Name")
        self.nm = QLineEdit()
        self.fboxLayout.addRow(self.l1, self.nm)
        btn = QPushButton("Search")
        btn.clicked.connect(self.__searchButtonClicked)
        self.fboxLayout.addRow(btn)
        self.formBoxGroup.setLayout(self.fboxLayout)

    def __searchButtonClicked(self):
        searchString = self.nm.text()

        if self.localBook.index is None:
            print("Warning... error")

        else:
            self.queryResult = self.localBook.searchForWords(searchString)




            self.init()
