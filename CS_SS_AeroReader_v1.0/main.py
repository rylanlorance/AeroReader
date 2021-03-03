from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout
import View.TabTableWidget as TabTableWidgetFile

from PyQt5.QtGui import QIcon
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("AeroReader!")
        self.width = 500
        self.height = 600
        self.setFixedSize(self.width, self.height)

        self.menuBar = QtWidgets.QMenuBar(self)


        # set up the menu


        # self.table_widget = TabTableWidgetFile.MyTableWidget(self)
        # self.setCentralWidget(self.table_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec())
