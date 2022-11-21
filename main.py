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
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('123')
        self.btn = QPushButton('Draw', self)
        self.btn.move(70, 150)
        self.btn.resize(60, 40)
        self.qp = QPainter()
        self.flag = False
        self.btn.clicked.connect(self.pushButtonEvent)

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
        self.qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        self.qp.drawEllipse(100, 100, a, a)

    def pushButtonEvent(self):
        self.drawz()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())