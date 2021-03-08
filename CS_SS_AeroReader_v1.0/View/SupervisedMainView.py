from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

import sys


class SupervisedMainView(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.mainVBox = QVBoxLayout()
        self.setLayout(self.mainVBox)

        self.formGroupBox = QGroupBox(title="MyGroupBox")
        self.fbox = QFormLayout()
        self.fbox.setAlignment(Qt.AlignLeft)
        self.__createFormBox()
        self.mainVBox.addWidget(self.formGroupBox)

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

    def __searchButtonClicked(self):
        searchString = self.searchBar.text()
        print("Working with the following : [{0}]".format(searchString))
        searchString.lower()
