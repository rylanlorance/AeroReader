from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5 import QtCore

import sys


class SupervisedSearchItemRow(QWidget):
    def __init__(self, parent, mySearchItem):
        super(QWidget, self).__init__(parent)
        self.rowVBox = QVBoxLayout()

        self.setStyleSheet("background-color: grey")

        self.setLayout(self.rowVBox)
        self.l1 = QLabel()
        self.l1.setText("Row ! ")
        self.rowVBox.addWidget(self.l1)



