from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QStackedLayout, \
    QStackedWidget, QDockWidget, QToolBar, QToolButton

# Modules
import View.TabTableWidget as TabTableWidgetFile
import View.SupervisedMainView as SupervisedViewFile
import View.FileSystemsWidget as FileSystemsWidgetFile
import View.TextViewerMain as TextViewerMainFile

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

        # file systems page for users to upload files
        self.f_s = FileSystemsWidgetFile.FileSystemsDialogueWidget(self)

        # view txt and pdf files
        self.txt_view = TextViewerMainFile.TextViewerMain(self)

        self.flow_stack = QStackedWidget()


        # self.flow_stack.addWidget(self.f_s)
        self.flow_stack.addWidget(self.txt_view)
        self.flow_stack.addWidget(self.supervisedWidget)

        # self.main_VBox = QVBoxLayout()
        # self.main_VBox.addWidget(self.flow_stack)

        self.setCentralWidget(self.flow_stack)

        self.createToolBar()



    def createToolBar(self):
        self.tb = QToolBar()

        self.tb_back_btn = QToolButton()
        self.tb_back_btn.setText("Back")
        self.tb_back_btn.clicked.connect(self.goToPreviousScreen)
        self.tb.addWidget(self.tb_back_btn)


        self.tb_next_btn = QToolButton()
        self.tb_next_btn.setText("Next")
        self.tb_next_btn.clicked.connect(self.goToNextScreen)
        self.tb.addWidget(self.tb_next_btn)


        self.addToolBar(Qt.BottomToolBarArea, self.tb)

        # self.main_VBox.addWidget(self.tb)


    def goToPreviousScreen(self):
        print("Let's go to the previous screen global")
        self.flow_stack.setCurrentIndex(self.flow_stack.currentIndex() - 1)

    def goToNextScreen(self):
        print("Let's go to next screen global")
        self.flow_stack.setCurrentIndex(self.flow_stack.currentIndex() + 1)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec())
