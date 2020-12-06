import random
import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, \
    QMessageBox


class MyWindow (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(0, 0, 600, 600)
        self.setFixedSize(600, 600)
        self.setWindowTitle('Oder in McDonald')
        grid = QGridLayout()
        self.setLayout(grid)

        mylabel = QLabel('Menu')
        mylabel.setAlignment(Qt.AlignHCenter)
        mylabel.setFont(QFont('Times', 22, QFont.Bold, QFont.StyleItalic))
        grid.addWidget(mylabel, 0,0)

        buttons = {}

        values = {}

        icons = []

        f = open("icons.txt", "r")

        for line in f.readlines():
            icons.append(line.rstrip())

        for i in range(1, 7):
            for j in range(0, 6):
                buttons[(i,j)] = QPushButton()
                buttons[(i,j)].resize(100, 100)
                buttons[(i,j)].setMaximumWidth(100)
                buttons[(i,j)].setMaximumHeight(100)
                buttons[(i,j)].setIcon(QIcon(icons.pop()))
                buttons[(i,j)].setIconSize(QSize(100, 100))
                buttons[(i,j)].clicked.connect(self.add)
                grid.addWidget(buttons[(i,j)], i, j)
                values[(i,j)] = random.randint(10,35)

        self.show()

        f.close()

    def add(self):
        QMessageBox.information(self, "Informacja", "Dodano do zamowienia")


def main():
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
