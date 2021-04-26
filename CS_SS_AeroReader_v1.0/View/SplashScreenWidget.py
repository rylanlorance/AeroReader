from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5 import QtCore

from pprint import pprint

import sys


class SplashScreenWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__()
        self.rowVBox = QHBoxLayout()
        self.setLayout(self.rowVBox)

        self.im = QPixmap("Resources/AeroReader_Logo.png")

        self.label = QLabel()

        self.label.setPixmap(self.im)

        self.rowVBox.addWidget(self.label, Qt.AlignCenter)

