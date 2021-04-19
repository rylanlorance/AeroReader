from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5 import QtCore

import sys

class SupervisedSearchResults(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.vbox = QVBoxLayout()
