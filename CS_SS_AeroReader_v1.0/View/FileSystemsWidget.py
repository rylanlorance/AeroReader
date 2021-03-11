from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QFileDialog

class FileSystemsDialogueWidget(QWidget):
    def __init__(self, parent):
        super(FileSystemsDialogueWidget, self).__init__(parent)
        self.v_layout = QVBoxLayout()

        # click button to open file systems
        self.btn = QPushButton("Q File Open")
        self.btn.clicked.connect(self.__getFiles)
        self.v_layout.addWidget(self.btn)

        self.setLayout(self.v_layout)

    def __getFiles(self):
        print("Getting File systems")
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        filenames = []

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read()
                print(data)

