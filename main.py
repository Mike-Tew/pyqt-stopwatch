import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from stopwatch import Stopwatch


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stopwatch")

        widget = qtw.QWidget()
        widget.setLayout(qtw.QHBoxLayout())

        self.sw1 = Stopwatch()
        widget.layout().addWidget(self.sw1)
        self.sw2 = Stopwatch()
        widget.layout().addWidget(self.sw2)
        self.setCentralWidget(widget)

        self.show()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()

    sys.exit(app.exec_())
