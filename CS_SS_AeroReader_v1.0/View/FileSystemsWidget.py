from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QFileDialog


class FileSystemsDialogueWidget(QWidget):
    def __init__(self, parent):
        super(FileSystemsDialogueWidget, self).__init__(parent)
        v_layout = QVBoxLayout()

        # click button to open file systems
        self.btn = QPushButton("Q File Open")
        self.btn.clicked.connect(self.getFiles)

    def __getFiles(self):
        print("Getting File systems")
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)

