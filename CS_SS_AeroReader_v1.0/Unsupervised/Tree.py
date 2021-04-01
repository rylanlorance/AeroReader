import sys

from argparse import ArgumentParser

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Clustering import TextCluster

# class for scrollable label
class ScrollLabel(QScrollArea):
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        # making widget resizable
        self.setWidgetResizable(True)

        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)

        # vertical box layout
        lay = QVBoxLayout(content)

        # creating label
        self.label = QLabel(content)

        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # making label multi-line
        self.label.setWordWrap(True)

        # adding label to the layout
        lay.addWidget(self.label)

    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)

class ClusterInformation(QWidget):
    def __init__(self, cluster: TextCluster.Cluster):
        super().__init__()

        layout = QVBoxLayout()

        self.words = QLabel(f'Words: {", ".join(cluster.frequent_words)}')
        self.pages = QLabel(f'Pages: {", ".join(map(str, cluster.page_numbers))}')

        layout.addWidget(self.words)
        layout.addWidget(self.pages)

        # creating scroll label
        self.page = ScrollLabel(self)

        # setting text to the label
        self.page.setText('Example Page:' + '\n\n' + cluster.example_page)

        layout.addWidget(self.page)

        self.setLayout(layout)

class Tree(QMainWindow):
    def __init__(self, book_file: str, depth: int, min_width: float, min_length: float,
                 button_width: int = 90, button_height: int = 20):
        QMainWindow.__init__(self)

        self.depth = depth

        self.positions = None
        self.button_height, self.button_width = button_height, button_width

        # You will always have this many buttons
        n_buttons = 2 ** (depth + 1) - 1

        # self.showFullScreen()
        self.setMinimumSize(QSize(min_width, min_length))
        self.setWindowTitle('Unsupervised Analysis')

        self.options = [QPushButton(str(n), self) for n in range(n_buttons)]

        self.change_button_positions()

        for n, button in enumerate(self.options):
            button.clicked.connect(
                self.show_new_window_n(n)
            )

        self.clusters = TextCluster(book_file, n_clusters=n_buttons).tree_analysis()
        self.cluster_info = None

    def change_button_positions(self):
        width, length = self.frameGeometry().width(), self.frameGeometry().height()

        self.positions = Tree.make_positions(self.depth, 0, 10, width - 100, length - 100)

        for i in range(self.depth + 1):
            for j in range(2 ** i, 2 ** (i + 1)):
                j -= 1
                self.options[j].setGeometry(self.positions[j][0], self.positions[j][1],
                                            self.button_width, self.button_height)

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

        for j in range(2 ** depth, 2 ** (depth + 1)):
            j -= 1
            dx = 10 if j % 2 == 0 else - 20

            positions[j] = (positions[j][0] + dx, positions[j][1])

        return positions

    def resizeEvent(self, a0) -> None:
        self.change_button_positions()

    def paintEvent(self, a0) -> None:
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(QPen(Qt.black, 8, Qt.SolidLine))
        painter.setBrush(Qt.white)

        n = len(self.positions)

        i = 0
        while i < n // 2:
            px, py = self.positions[i]
            cx, cy = self.positions[2*i + 1]

            px += self.button_width // 2
            py += self.button_height // 2

            cx += self.button_width // 2
            cy += self.button_height // 2

            painter.drawLine(px, py, cx, cy)

            cx, cy = self.positions[2 * i + 2]

            cx += self.button_width // 2
            cy += self.button_height // 2

            painter.drawLine(px, py, cx, cy)

            i += 1

    def show_new_window_n(self, n):

        def show_window(checked):
            self.cluster_info = ClusterInformation(self.clusters[n])
            self.cluster_info.show()

        return show_window

if __name__ == '__main__':
    args = ArgumentParser()
    args.add_argument('file', help='PDF book to analyze')
    args.add_argument('--depth', help='Depth of binary tree', type=int, default=4)
    args = args.parse_args()

    # Depending on the depth set, screen settings change

    if args.depth < 1 or args.depth > 5:
        raise ValueError('depth must be a natural number less than five.')

    button_width = {
        1: 90,
        2: 90,
        3: 70,
        4: 60,
        5: 30,
    }

    width = {
        1: 500,
        2: 500,
        3: 800,
        4: 1300,
        5: 1500,
    }

    height = {
        1: 500,
        2: 500,
        3: 700,
        4: 800,
        5: 900,
    }

    app = QApplication(sys.argv)
    mainWin = Tree(args.file, depth=args.depth, min_width=width[args.depth], min_length=height[args.depth],
                   button_width=button_width[args.depth])
    mainWin.show()
    sys.exit(app.exec_())
