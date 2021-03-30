import os

from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QFileDialog, QBoxLayout, \
    QHBoxLayout, QGroupBox, QFrame, QMessageBox
from PyQt5.uic.properties import QtGui

from Data.Book import Book


class FileSystemsDialogueWidget(QWidget):
    def __init__(self, parent):
        super(FileSystemsDialogueWidget, self).__init__()
        self.parent = parent
        self.v_layout = QVBoxLayout()

        self.addDocumentsBox = QGroupBox("Add Documents")
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
        container.setStyleSheet("background-color: grey")

        l1 = Qt.QLabel("Drag and Drop (Under Construction)")

        btn = Qt.QPushButton("Click to browse files")
        btn.clicked.connect(self.__getFiles)

        docs_box.addWidget(l1)
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

        # create a book object to hold all book information
        myBook = Book()
        myBook.file_type = file_ext
        print("mybook.filetype: ", myBook.file_type)

        acceptable_filetypes = [".txt", ".pdf"]

        if myBook.file_type in acceptable_filetypes:
            print("We have an acceptable filetype")

            ##
            if myBook.file_type == ".pdf":


        else:
            self.wrongFilePopup = QMessageBox()

            ## add message box




    def __fs_goToNextScreen(self):
        print("Going to next screen local")
        self.parent.goToNextScreen()
