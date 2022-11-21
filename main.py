import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Task_2.ui', self)
        self.qp = QPainter()
        self.flag = False
        self.pushButton.clicked.connect(self.pushButtonEvent)

    def drawz(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)

            self.draw()
            self.qp.end()

    def draw(self):
        a = random.randint(1, 255)
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(100, 100, a, a)

    def pushButtonEvent(self):
        self.drawz()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())