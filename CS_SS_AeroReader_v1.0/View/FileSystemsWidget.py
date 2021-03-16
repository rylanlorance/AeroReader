from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QFileDialog, QBoxLayout, \
    QHBoxLayout


class FileSystemsDialogueWidget(QWidget):
    def __init__(self, parent):
        super(FileSystemsDialogueWidget, self).__init__()
        self.parent = parent
        self.v_layout = QVBoxLayout()

        # click button to open file systems
        self.btn = QPushButton("Q File Open")
        self.btn.clicked.connect(self.__getFiles)
        self.btn.resize(60, 60)

        self.v_layout.addWidget(self.btn, alignment=QtCore.Qt.AlignTop)

        self.__createBtn()

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

    def __createBtn(self):
        self.h_box = QHBoxLayout()
        self.nextScreenBtn = QPushButton("Next Screen")
        self.nextScreenBtn.clicked.connect(self.__fs_goToNextScreen)
        # self.nextScreenBtn.clicked.connect(super.goToNextScreen())
        self.previousScreenBtn = QPushButton("Previous Screen")

        self.h_box.addWidget(self.nextScreenBtn, alignment=QtCore.Qt.AlignBottom)
        self.h_box.addWidget(self.previousScreenBtn)
        self.v_layout.addLayout(self.h_box)

    def __fs_goToNextScreen(self):
        print("Going to next screen local")
        self.parent.goToNextScreen()


