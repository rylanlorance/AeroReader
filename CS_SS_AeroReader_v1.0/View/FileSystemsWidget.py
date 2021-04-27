import os

from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QFileDialog, QBoxLayout, \
    QHBoxLayout, QGroupBox, QFrame, QMessageBox


class FileSystemsDialogueWidget(QWidget):
    def __init__(self, parent):
        super(FileSystemsDialogueWidget, self).__init__()
        self.parent = parent
        self.v_layout = QVBoxLayout()

        self.localBook = self.parent.myBook

        self.addDocumentsBox = QGroupBox("Add Documents")
        self.addDocumentsBox.setStyleSheet("background-color: rgb(233, 237, 201)")
        self.addDocumentsBox.setFixedSize(400, 500)
        self.addDocumentsBoxLayout = QVBoxLayout()

        self.addDocumentsBox.setLayout(self.addDocumentsBoxLayout)
        self.buildDocumentsBoxUI()

        self.v_layout.addWidget(self.addDocumentsBox)

        # self.v_layout.addWidget(self.btn, alignment=QtCore.Qt.AlignTop)

        self.setLayout(self.v_layout)


    def buildDocumentsBoxUI(self):
        print("Building Docs Box")
        docs_box = QVBoxLayout()
        container = QWidget()
        container.setLayout(docs_box)
        container.setFixedSize(200, 200)
        container.setStyleSheet("background-color: rgb(204, 213, 174)")

        # l1 = Qt.QLabel("Drag and Drop (Under Construction)")

        btn = Qt.QPushButton("Click to browse files")
        btn.clicked.connect(self.__getFiles)

        docs_box.addWidget(btn)
        self.addDocumentsBoxLayout.addWidget(container, alignment=QtCore.Qt.AlignHCenter)


    def __getFiles(self):
        print("Getting File systems")
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        filenames = []

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')
            # file_info = os.path.splitext(f.name)
            # print("1st info", file_info[0])
            # print("2nd name", file_info[1])

            with f:
                self.__UploadBook(f)
                # print("F equals", f)
                # data = f.read()
                # print(data)

    def __UploadBook(self, file):
        print("File = ", file)
        file_info = os.path.splitext(file.name)
        file_name = file_info[0]
        file_ext = file_info[1]
        print("File ext-", file_ext)

        # create a book object to hold all book information
        self.localBook.file_type = str(file_ext)

        acceptable_filetypes = [".txt", " .pdf", " .txt", " .pdf"]

        if self.localBook.file_type == ".txt" or self.localBook.file_type == ".pdf":
            print("We have an acceptable file type")
            self.localBook.setBook(file)

        else:
            print("We have an unacceptable file type")

        self.save()


    def save(self):
        self.parent.setBook(self.localBook)

    def __fs_goToNextScreen(self):
        print("Going to next screen local")
        self.parent.goToNextScreen()
