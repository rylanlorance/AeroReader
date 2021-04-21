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

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)

        widget = QWidget()
        self.scrollArea.setWidget(widget)
        scrollLayout = QVBoxLayout(widget)

        for i in range(5):
            newRow = SupervisedSearchItemRow(self)
            scrollLayout.addWidget(newRow)

        scrollLayout.addStretch(1)


        self.queryFormBoxLayout.addWidget(self.scrollArea)



        # for i in range(0, 10):
        #     self.queryFormBoxLayout.addWidget(QLabel("Fuck"))

        # resultRow = SupervisedSearchItemRow(self)
        # vbox_scroll_layout.addWidget(resultRow)
        #
        # resultRow1 = SupervisedSearchItemRow(self)
        # vbox_scroll_layout.addWidget(resultRow1)
        #
        # resultRow2 = SupervisedSearchItemRow(self)
        # vbox_scroll_layout.addWidget(resultRow2)
        #

        #
        # resultRow1 = SupervisedSearchItemRow(self)
        # self.queryFormBoxLayout.addWidget(resultRow1)
        #
        # resultRow2 = SupervisedSearchItemRow(self)
        # self.queryFormBoxLayout.addWidget(resultRow2)


        # resultRow = SupervisedSearchItemRow(self)
        # self.queryFormBoxLayout.addWidget(resultRow)
        #
        # resultRow1 = SupervisedSearchItemRow(self)
        # self.queryFormBoxLayout.addWidget(resultRow1)
        #
        # resultRow2 = SupervisedSearchItemRow(self)
        # self.queryFormBoxLayout.addWidget(resultRow2)





        for loc in self.queryResult.queryLocations:
            print("Query location obj = ", loc)
            print("Query location obj info = ", loc.word)
            print("Query location obj line pos = ", loc.line_pos)
            print("Query location obj word pos = ", loc.word_pos)

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
