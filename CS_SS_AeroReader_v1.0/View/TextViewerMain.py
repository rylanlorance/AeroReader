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

        self.text_box = QTextEdit()
        self.__setTextEditorSettings()

        self.mainVBox.addWidget(self.text_box)

    def __setTextEditorSettings(self):
        self.text_box.setAutoFormatting(QTextEdit.AutoAll)
        font = QFont('Times', 24)
        self.text_box.setFont(font)
        self.text_box.setText("""I found a dimpled spider, fat and white,
On a white heal-all, holding up a moth
Like a white piece of rigid satin cloth--
Assorted characters of death and blight
Mixed ready to begin the morning right,
Like the ingredients of a witches' broth--
A snow-drop spider, a flower like a froth,
And dead wings carried like a paper kite.

What had that flower to do with being white,
The wayside blue and innocent heal-all?
What brought the kindred spider to that height,
Then steered the white moth thither in the night?
What but design of darkness to appall?--
If design govern in a thing so small."
I found a dimpled spider, fat and white,
On a white heal-all, holding up a moth
Like a white piece of rigid satin cloth--
Assorted characters of death and blight
Mixed ready to begin the morning right,
Like the ingredients of a witches' broth--
A snow-drop spider, a flower like a froth,
And dead wings carried like a paper kite.""")
