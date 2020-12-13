import random
import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, \
    QMessageBox


class MyWindow (QWidget):

    values = {}

    buttons = {}

    icons = []

    orderCost = 0

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 600, 600)
        self.setFixedSize(600, 600)
        self.setWindowTitle('Order in McDonald')
        grid = QGridLayout()
        self.setLayout(grid)

        mylabel = QLabel('Menu')
        mylabel.setAlignment(Qt.AlignHCenter)
        mylabel.setFont(QFont('Times', 22, QFont.Bold, QFont.StyleItalic))
        grid.addWidget(mylabel, 0,0)


        shoppingButton = QPushButton()
        shoppingButton.resize(50, 50)
        shoppingButton.setMaximumWidth(50)
        shoppingButton.setMaximumHeight(50)
        shoppingButton.setIcon(QIcon("shopping.png"))
        shoppingButton.setIconSize(QSize(50, 50))
        grid.addWidget(shoppingButton, 0, 5)

        iconsFile = open("icons.txt", "r")
        dataFile = open("data.txt", "r")

        for line in iconsFile.readlines():
            self.icons.append(line.rstrip())

        font = QFont()
        font.setPointSize(1)

        for i in range(1, 7):
            for j in range(0, 6):
                self.values[(i, j)] = random.randint(10, 35)
                self.buttons[(i,j)] = QPushButton()
                self.buttons[(i,j)].setText(dataFile.readline())
                self.buttons[(i,j)].setFont(font)
                self.buttons[(i,j)].resize(100, 100)
                self.buttons[(i,j)].setMaximumWidth(100)
                self.buttons[(i,j)].setMaximumHeight(100)
                self.buttons[(i,j)].setIcon(QIcon(self.icons.pop()))
                self.buttons[(i,j)].setIconSize(QSize(100, 100))
                self.buttons[(i,j)].clicked.connect(self.confirmation)
                grid.addWidget(self.buttons[(i,j)], i, j)

        self.show()

        iconsFile.close()
        dataFile.close()

    def add(self):
        QMessageBox.information(self, "Informacja", "Dodano do zamowienia")
        sender = self.sender()
        stringOrderCost = sender.text()[-3:]
        self.orderCost = int(stringOrderCost)

    def confirmation(self, event):
        sender = self.sender()
        question = "Do you want add this product to your order?\n" + sender.text()
        choice = QMessageBox.question(self, 'Confirmation', question,
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            self.add()

def main():
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
