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

        self.formBoxGroup = QGroupBox("Search Group")

        self.__createFormBox()

        self.mainVBox.addWidget(self.formBoxGroup)

        self.spacerBtn = QPushButton()
        self.spacerBtn.setText("SpacerButton")
        self.mainVBox.addWidget(self.spacerBtn)

        self.searchItemRow = SupervisedSearchItemRow(parent, "mySearchString")
        self.mainVBox.addWidget(self.searchItemRow)

        self.btnBox = QHBoxLayout()
        self.nextBtn = QPushButton("Next Screen")
        self.nextBtn = QPushButton("Previous Screen")


    def __createFormBox(self):
        self.fboxLayout = QFormLayout()
        l1 = QLabel("Name")
        nm = QLineEdit()
        self.fboxLayout.addRow(l1, nm)
        self.formBoxGroup.setLayout(self.fboxLayout)

    def __searchButtonClicked(self):
        searchString = self.searchBar.text()
        print("Working with the following : [{0}]".format(searchString))
        searchString.lower()

    def __loadSearchResults(self, searchString):
        # try this
        sr1 = SearchResult()
        sr2 = SearchResult()
        print("Loading Search Screen")
