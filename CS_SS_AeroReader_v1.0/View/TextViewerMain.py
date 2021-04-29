import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRect
from PyQt5 import QtCore
from PyQt5.QtGui import *

# class borrowed from https://learndataanalysis.org/highlighting-specific-line-in-a-text-editor-pyqt5-tutorial/

class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super().__init__(parent)
        self._highlight_lines = {}

    def highlight_line(self, line_num, fmt):
        if isinstance(line_num, int) and line_num >= 0 and isinstance(fmt, QTextCharFormat):
            self._highlight_lines[line_num] = fmt
            block = self.document().findBlockByLineNumber(line_num)
            self.rehighlightBlock(block)

    def clear_highlight(self):
        self._highlight_lines = {}
        self.rehighlight()

    def highlightBlock(self, text):
        blockNumber = self.currentBlock().blockNumber()
        fmt = self._highlight_lines.get(blockNumber)
        if fmt is not None:
            self.setFormat(0, len(text), fmt)


class TextViewerMain(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.mainVBox = QVBoxLayout()
        self.setLayout(self.mainVBox)
        self.parent = parent
        self.localBook = self.parent.getBook()

        self.openUnsupervisedWidgetBtn = QPushButton("Open Unsupervised")
        self.openUnsupervisedWidgetBtn.setStyleSheet("background-color: rgb(69, 123, 157)")
        self.openUnsupervisedWidgetBtn.clicked.connect(parent.initUnsupervisedWindow)
        self.mainVBox.addWidget(self.openUnsupervisedWidgetBtn)

        self.openSupervisedWidgetBtn = QPushButton("Open Supervised")
        self.openSupervisedWidgetBtn.setStyleSheet("background-color: rgb(168, 218, 220)")
        self.openSupervisedWidgetBtn.clicked.connect(parent.initSupervisedWindow)
        self.mainVBox.addWidget(self.openSupervisedWidgetBtn)

        self.text_box = QPlainTextEdit()
        self.text_box.setWordWrapMode(QTextOption.NoWrap)
        self.setTextEditorSettings()
        self.text_box.setStyleSheet("background-color: rgb(250, 237, 205)")

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

        format = QTextCharFormat()
        format.setBackground(Qt.yellow)

        self.highlighter = SyntaxHighlighter(self.text_box.document())

        self.highlighter.clear_highlight()

        try:
            self.highlighter.highlight_line(line_pos, format)

        except ValueError:
            print("Error Highlighting")

        self.lineCursor = QTextCursor(self.text_box.document().findBlockByLineNumber(line_pos))
        self.text_box.setTextCursor(self.lineCursor)

