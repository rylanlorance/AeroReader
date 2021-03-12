from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QStackedLayout, \
    QStackedWidget, QDockWidget

import View.TabTableWidget as TabTableWidgetFile
import View.SupervisedMainView as SupervisedViewFile
import View.FileSystemsWidget as FileSystemsWidgetFile

from PyQt5.QtGui import QIcon
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("AeroReader!")
        self.width = 1000
        self.height = 700
        self.setGeometry(QtCore.QRect(0, 0, self.height, self.width))

        # set up Supervised View- @Darby if you want to show your view instead, just comment out the two following
        # lines.
        self.supervisedWidget = SupervisedViewFile.SupervisedMainView(self)

        self.f_s = FileSystemsWidgetFile.FileSystemsDialogueWidget(self)

        self.flow_stack = QStackedWidget()

        self.flow_stack.addWidget(self.f_s)
        self.flow_stack.addWidget(self.supervisedWidget)

        self.main_VBox = QVBoxLayout()
        self.main_VBox.addWidget(self.flow_stack)

        self.setCentralWidget(self.flow_stack)

    def goToNextScreen(self):
        print("Let's go to next screen global")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec())
