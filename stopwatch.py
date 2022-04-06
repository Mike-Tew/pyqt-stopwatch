from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class Stopwatch(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QVBoxLayout())

        self.display_label = qtw.QLabel("00:00:00.00")
        self.display_label.setFont(qtg.QFont("Helvetica", 30))
        self.layout().addWidget(self.display_label)

        self.start_button = qtw.QPushButton("START")
        self.start_button.clicked.connect(self.close)
        self.layout().addWidget(self.start_button)


        print("Got em")