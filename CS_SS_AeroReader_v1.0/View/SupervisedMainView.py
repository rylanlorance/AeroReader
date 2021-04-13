from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRect
from PyQt5 import QtCore
from PyQt5.QtGui import *

import sys

from Data.SearchResult import SearchResult
from View.SupervisedSearchItemRow import SupervisedSearchItemRow


class SupervisedMainView(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.mainVBox = QVBoxLayout()
        self.setLayout(self.mainVBox)
        self.parent = parent

        self.localBook = self.parent.getBook()

        self.formBoxGroup = QGroupBox("Search Group")

        self.__createFormBox()

        self.mainVBox.addWidget(self.formBoxGroup)

        self.searchItemRow = SupervisedSearchItemRow(parent, "mySearchString")
        self.mainVBox.addWidget(self.searchItemRow)

        self.searchListArea = QScrollArea()
        self.createSearchListArea()

    def init(self):
        self.localBook = self.parent.getBook()

    def createSearchListArea(self):
        self.searchListArea.setWidgetResizable(True)
        self.groupBox = QGroupBox()



    def __createFormBox(self):
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
        print("Working with the following : [{0}]".format(searchString))
        self.localBook.searchForWords(searchString)




