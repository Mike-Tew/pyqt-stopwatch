from time import time

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class Stopwatch(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.total_time = 0
        self.paused_time = 0

        self.setLayout(qtw.QGridLayout())

        self.display_label = qtw.QLabel("00:00:00.00")
        self.display_label.setFont(qtg.QFont("Helvetica", 30))
        self.layout().addWidget(self.display_label, 0, 0, 1, 3)

        self.start_button = qtw.QPushButton("START")
        self.start_button.clicked.connect(self.show_text)
        self.layout().addWidget(self.start_button, 1, 0)

        self.stop_button = qtw.QPushButton("STOP")
        self.layout().addWidget(self.stop_button, 1, 1)

        self.reset_button = qtw.QPushButton("RESET")
        self.layout().addWidget(self.reset_button, 1, 2)

    def show_text(self):
        print("Got em")
        self.elapsed_time = time()
        print(self.elapsed_time)