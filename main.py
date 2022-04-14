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
        save_icon = self.style().standardIcon(qtw.QStyle.SP_TitleBarMenuButton)
        file_menu.addAction(save_icon, "Add Timer", self.add_timer)
        file_menu.addAction("Exit", self.close)

        # Central Widget
        self.widget = qtw.QWidget()
        self.widget.setLayout(qtw.QHBoxLayout())
        self.setCentralWidget(self.widget)
        self.widget.layout().addWidget(Stopwatch())

        # Status Bar
        self.statusBar().showMessage("Stopwatch Added")
        self.show()

    def add_timer(self):
        self.widget.layout().addWidget(Stopwatch())
        self.statusBar().showMessage("Stopwatch Added")



if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()

    sys.exit(app.exec_())
