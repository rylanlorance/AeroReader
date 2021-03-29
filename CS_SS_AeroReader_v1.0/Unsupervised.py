import sys
from turtle import width

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QMenu
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, QTimer


class Tree(QMainWindow):
    def __init__(self, depth: int, min_width: float, min_length: float):
        QMainWindow.__init__(self)

        self.depth = depth

        # You will always have this many buttons
        n_buttons = 2 ** (depth + 1) - 1

        # self.showFullScreen()
        self.setMinimumSize(QSize(min_length, min_width))
        self.setWindowTitle('Unsupervised Version')

        self.options = {n: QPushButton(str(n), self) for n in range(n_buttons)}

        self.change_button_positions()

    def change_button_positions(self):
        width, length = self.frameGeometry().width(), self.frameGeometry().height()

        positions = Tree.make_positions(self.depth, 0, 10, width - 100, length - 100)

        for i in range(self.depth):
            for j in range(2 ** i, 2 ** (i + 1)):
                j -= 1
                self.options[j].move(positions[j][0], positions[j][1])

        for j in range(2 ** self.depth, 2 ** (self.depth + 1)):
            j -= 1
            dx = 10 if j % 2 == 0 else - 20
            self.options[j].move(positions[j][0] + dx, positions[j][1])

    @staticmethod
    def make_positions(depth, x, y, w, l):
        """Generate positions array for binary tree of depth inside a rectangle with width w and length l with top left
        corner x, y """

        positions = [None] * (2 ** (depth + 1) - 1)

        dy = (l - y) // depth

        ly = l + y
        dx = (w - x) // (2 ** (depth - 1))

        # First we initialize bottom row
        j = 0
        for i in list(range(2 ** (depth - 1) - 1, 2 ** depth - 1)):
            left = x + dx * j
            right = left + dx

            third = (right - left) // 3

            positions[2 * i + 1] = (left + third, ly)
            positions[2 * i + 2] = (left + 2 * third, ly)

            j += 1

        for d in range(depth, -1, -1):
            for i in list(range(int(2 ** (d - 1) - 1), int(2 ** d - 1))):
                lx, y = positions[2 * i + 1]
                rx, _ = positions[2 * i + 2]

                positions[i] = (lx + (rx - lx) // 2, y - dy)

        return positions

    def resizeEvent(self, a0) -> None:
        self.change_button_positions()

# this will open our tree app
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = Tree(3, 900, 900)
    mainWin.show()
    sys.exit(app.exec_())
