from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5 import QtCore

from pprint import pprint

import sys


class SupervisedSearchItemRow(QWidget):
    def __init__(self, parent, SearchResItem, lineContext):
        super(QWidget, self).__init__()
        self.rowHBox = QHBoxLayout()
        self.parent = parent
        self.SearchResItem = SearchResItem
        self.setStyleSheet("border: 1px solid black")
        self.rowVBox = QVBoxLayout()

        self.label = QLabel(SearchResItem.word)
        self.label.setFont(QFont('Arial', 15))
        self.rowVBox.addWidget(self.label)

        self.line = QLabel(lineContext)
        self.rowVBox.addWidget(self.line)

        self.rowHBox.addLayout(self.rowVBox)

        self.goToButton = QPushButton("Go to usage")
        self.goToButton.clicked.connect(self.onUsageButtonPressed)
        self.rowHBox.addWidget(self.goToButton)

        self.setLayout(self.rowHBox)

    def onUsageButtonPressed(self):
        # moveLineCursor(self.SearchResItem.line_pos, self.SearchResItem.word_pos)

        self.parent.parent.moveCursorMain()








