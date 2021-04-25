from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5 import QtCore

from pprint import pprint
import sys


class SupervisedSearchItemRow(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.rowHBox = QHBoxLayout()
        self.parent = parent

        self.label = QLabel("Rylan Lorance")
        self.rowHBox.addWidget(self.label)



