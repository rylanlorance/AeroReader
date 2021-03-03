from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import View.TabTableWidget as TabTableWidgetFile

from PyQt5.QtGui import QIcon
import sys


# This is a sample Python script.
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("AeroReader!")
        self.width = 500
        self.height = 600
        self.setFixedSize(self.width, self.height)

        self.label = QtWidgets.QLabel(self)
        self.label.move(50, 50)
        self.table_widget = TabTableWidgetFile.MyTableWidget(self)
        self.setCentralWidget(self.table_widget)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec())
