import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import View.SupervisedMainView as SupervisedMainViewFile


class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.parent = parent

        # Init tabs
        self.tabs = QTabWidget()
        self.unsupervisedTab = QWidget()
        self.supervisedTab = SupervisedMainViewFile.SupervisedMainView(self)
        self.tabs.resize(300,200)

        # Add Tabs
        self.tabs.addTab(self.unsupervisedTab, "Unsupervised")
        self.tabs.addTab(self.supervisedTab, "Supervised")

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
