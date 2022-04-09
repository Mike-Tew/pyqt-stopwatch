import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from stopwatch import Stopwatch


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stopwatch")

        # Menu Bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        open_action = file_menu.addAction("Open", self.test_method)
        save_action = file_menu.addAction("Save")
        help_menu = menu_bar.addMenu("Help")
        about_menu = menu_bar.addMenu("About")

        # Central Widget
        widget = qtw.QWidget()
        widget.setLayout(qtw.QHBoxLayout())

        self.sw1 = Stopwatch()
        widget.layout().addWidget(self.sw1)
        self.sw2 = Stopwatch()
        widget.layout().addWidget(self.sw2)
        self.setCentralWidget(widget)

        # Status Bar
        self.statusBar().showMessage("GUI Activated")

        self.show()

    def test_method(self):
        print("Test method.")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()

    sys.exit(app.exec_())
