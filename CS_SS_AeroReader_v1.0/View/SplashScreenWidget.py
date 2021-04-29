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

        self.im = QPixmap("Resources/AeroReaderLogoV2.png")
        self.im2 = self.im.scaled(300, 300, Qt.KeepAspectRatio)

        self.label = QLabel()

        self.label.setPixmap(self.im2)

        self.rowVBox.addWidget(self.label, QtCore.Qt.AlignHCenter)

