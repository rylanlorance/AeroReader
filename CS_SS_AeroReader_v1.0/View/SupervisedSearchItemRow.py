from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5 import QtCore

import sys


class SupervisedSearchItemRow(QWidget):
    def __init__(self, parent, mySearchItem):
        super(QWidget, self).__init__(parent)
        self.rowVBox = QVBoxLayout()
        self.setLayout(self.rowVBox)

        self.setGeometry(QtCore.QRect(0, 0, 10, 21))
        self.setStyleSheet("background-color: grey")
