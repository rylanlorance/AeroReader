from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRect
from PyQt5 import QtCore
from PyQt5.QtGui import *


class TextViewerMain(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.mainVBox = QVBoxLayout()
        self.setLayout(self.mainVBox)
        self.parent = parent
        self.localBook = self.parent.getBook()

        self.openUnsupervisedWidgetBtn = QPushButton("Open Unsupervised")
        self.mainVBox.addWidget(self.openUnsupervisedWidgetBtn)

        self.openSupervisedWidgetBtn = QPushButton("Open Supervised")
        self.openSupervisedWidgetBtn.clicked.connect(parent.initSupervisedWindow)
        self.mainVBox.addWidget(self.openSupervisedWidgetBtn)

        self.text_box = QPlainTextEdit()
        self.text_box.setWordWrapMode(QTextOption.NoWrap)
        self.setTextEditorSettings()

        self.mainVBox.addWidget(self.text_box)

        # important information

        self.lineCursor = QTextCursor()

        # linecursor = QTextCursor(self.text_box.document().findBlockByLineNumber(250 - 1))
        # self.text_box.setTextCursor(linecursor)

    def setTextEditorSettings(self):
        self.localBook = self.parent.getBook()

        print("Current Book: ", self.localBook.contents)

        self.text_box.setReadOnly(True)
        font = QFont('Times', 24)
        self.text_box.setFont(font)
        self.text_box.clear()

        if self.localBook.contents is None:
            self.text_box.insertPlainText("No Book Uploaded yet")

        else:
            self.text_box.insertPlainText(self.localBook.contents)

    def moveLine(self, line_pos):
        print("Moved cursor to", line_pos)
        self.lineCursor = QTextCursor(self.text_box.document().findBlockByLineNumber(line_pos))
        self.text_box.setTextCursor(self.lineCursor)

