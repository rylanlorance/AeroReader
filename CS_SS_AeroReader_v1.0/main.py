from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout
import View.TabTableWidget as TabTableWidgetFile
import View.SupervisedMainView as SupervisedViewFile

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
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 500, 21))

        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.setMenuBar(self.menuBar)

        # set up Supervised View- @Darby if you want to show your view instead, just comment out the two following lines.

        self.supervisedWidget = SupervisedViewFile.SupervisedMainView(self)
        self.supervisedWidget.setGeometry(0, 0, 500, 800)

        # set up the menu

        # self.table_widget = TabTableWidgetFile.MyTableWidget(self)

        # self.setCentralWidget(self.table_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec())
