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

        f = open("icons.txt", "r")

        for line in f.readlines():
            self.icons.append(line.rstrip())

        for i in range(1, 7):
            for j in range(0, 6):
                self.values[(i, j)] = random.randint(10, 35)
                self.buttons[(i,j)] = QPushButton()
                self.buttons[(i,j)].setText(str(self.values[(i, j)]))
                self.buttons[(i,j)].resize(100, 100)
                self.buttons[(i,j)].setMaximumWidth(100)
                self.buttons[(i,j)].setMaximumHeight(100)
                self.buttons[(i,j)].setIcon(QIcon(self.icons.pop()))
                self.buttons[(i,j)].setIconSize(QSize(100, 100))
                self.buttons[(i,j)].clicked.connect(self.confirmation)
                grid.addWidget(self.buttons[(i,j)], i, j)


        self.show()

        f.close()

    def add(self):
        QMessageBox.information(self, "Informacja", "Dodano do zamowienia")
        sender = self.sender()
        self.orderCost = self.orderCost + int(sender.text())
        
	def confirmation(self, event):
		choice = QMessageBox.question(self, 'Confirmation', 'Do you want add this product to your order?',
                                      QMessageBox.Yes | QMessageBox.No)
		if choice == QMessageBox.Yes:
			self.add()


def main():
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
