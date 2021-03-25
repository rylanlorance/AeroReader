from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRect
from PyQt5 import QtCore
from PyQt5.QtGui import *


class TextViewerMain(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.mainVBox = QVBoxLayout()
        self.setLayout(self.mainVBox)

        self.l1 = QLabel("Hello Text Viewer")
        self.mainVBox.addWidget(self.l1)
        self.openUnsupervisedWidgetBtn = QPushButton("Open Unsupervised")
        self.mainVBox.addWidget(self.openUnsupervisedWidgetBtn)

        self.text_box = QPlainTextEdit()
        self.text_box.setWordWrapMode(QTextOption.NoWrap)
        self.__setTextEditorSettings()

        self.mainVBox.addWidget(self.text_box)

        # important information

        # linecursor = QTextCursor(self.text_box.document().findBlockByLineNumber(250 - 1))
        # self.text_box.setTextCursor(linecursor)


    def __setTextEditorSettings(self):
        self.text_box.setReadOnly(True)
        font = QFont('Times', 24)
        self.text_box.setFont(font)
        f = open("Meta/Metamorphasis_Kafka.txt")
        self.text_box.insertPlainText(f.read())

