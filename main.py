import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from stopwatch import Stopwatch


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stopwatch")

        self.setLayout(qtw.QHBoxLayout())

        self.sw1 = Stopwatch()
        self.layout().addWidget(self.sw1)
        self.sw2 = Stopwatch()
        self.layout().addWidget(self.sw2)

        self.show()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()

    sys.exit(app.exec_())
