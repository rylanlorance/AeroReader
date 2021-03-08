import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class SupervisedMainView(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.mainVBox = QVBoxLayout()
        self.setLayout(self.mainVBox)

        l1 = QLabel()
        l1.setText("Supervised Search Algorithm")

        self.mainVBox.addWidget(l1)
        self.mainVBox.addStretch()