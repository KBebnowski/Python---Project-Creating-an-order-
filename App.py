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
        self.setWindowTitle('Aplikacja Qt - Widget')
        grid = QGridLayout()
        self.setLayout(grid)

        mylabel = QLabel('Menu')
        mylabel.setAlignment(Qt.AlignHCenter)
        mylabel.setFont(QFont('Times', 22, QFont.Bold, QFont.StyleItalic))
        grid.addWidget(mylabel, 0,0)

        # btnBurger1 = QPushButton()
        # btnBurger1.resize(100, 100)
        # btnBurger1.setMaximumWidth(100)
        # btnBurger1.setMaximumHeight(100)
        # btnBurger1.setIcon(QIcon('burger.jpg'))
        # btnBurger1.setIconSize(QSize(100, 100))
        # btnBurger1.setIcon
        #
        # btnBurger2 = QPushButton()
        # btnBurger2.resize(100, 100)
        # btnBurger2.setMaximumWidth(100)
        # btnBurger2.setMaximumHeight(100)
        # btnBurger2.setIcon(QIcon('burger.jpg'))
        # btnBurger2.setIconSize(QSize(100, 100))
        # btnBurger2.setIcon
        #
        # btnBurger3 = QPushButton()
        # btnBurger3.resize(100, 100)
        # btnBurger3.setMaximumWidth(100)
        # btnBurger3.setMaximumHeight(100)
        # btnBurger3.setIcon(QIcon('burger.jpg'))
        # btnBurger3.setIconSize(QSize(100, 100))
        # btnBurger3.setIcon


        buttons = {}

        values = {}



        for i in range(1, 7):
            for j in range(0, 6):
                buttons[(i,j)] = QPushButton()
                buttons[(i,j)].resize(100, 100)
                buttons[(i,j)].setMaximumWidth(100)
                buttons[(i,j)].setMaximumHeight(100)
                buttons[(i,j)].setIcon(QIcon('burger.jpg'))
                buttons[(i,j)].setIconSize(QSize(100, 100))
                buttons[(i,j)].clicked.connect(self.add)
                grid.addWidget(buttons[(i,j)], i, j)
                values[(i,j)] = random.randint(10,35)

        self.show()


    def add(self):
        QMessageBox.information(self, "Informacja", "Dodano do zamowienia")


def main():
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
