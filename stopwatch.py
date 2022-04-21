from time import time

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class Stopwatch(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.current_time = 0
        self.paused_time = 0
        self.total_time = 0

        self.setLayout(qtw.QGridLayout())

        self.display_label = qtw.QLabel("00:00.00")
        self.display_label.setFont(qtg.QFont("Helvetica", 30))
        self.display_label.setAlignment(qtc.Qt.AlignCenter)

        self.layout().addWidget(self.display_label, 1, 0, 1, 3)

        self.start_button = qtw.QPushButton("START", clicked=self._on_start)
        self.start_button.clicked.connect(self._on_start)
        start_icon = self.style().standardIcon(qtw.QStyle.SP_MediaPlay)
        self.start_button.setIcon(start_icon)
        self.layout().addWidget(self.start_button, 2, 0)

        self.pause_button = qtw.QPushButton("PAUSE", clicked=self._on_pause)
        pause_icon = self.style().standardIcon(qtw.QStyle.SP_MediaPause)
        self.pause_button.setIcon(pause_icon)
        self.pause_button.setEnabled(False)
        self.layout().addWidget(self.pause_button, 2, 1)

        self.reset_button = qtw.QPushButton("RESET", clicked=self._on_reset)
        reset_icon = self.style().standardIcon(qtw.QStyle.SP_BrowserReload)
        self.reset_button.setIcon(reset_icon)
        self.reset_button.setEnabled(False)
        self.layout().addWidget(self.reset_button, 2, 2)

        self.close_button = qtw.QPushButton(clicked=self.deleteLater)
        close_icon = self.style().standardIcon(qtw.QStyle.SP_MessageBoxCritical)
        self.close_button.setIcon(close_icon)
        self.layout().addWidget(self.close_button, 2, 3)

        self.setFixedSize(350, 200)

        # Timer
        self.timer = qtc.QTimer(self)
        self.timer.timeout.connect(self.show_time)

    def _on_start(self):
        self.start_button.setEnabled(False)
        self.pause_button.setEnabled(True)
        self.reset_button.setEnabled(True)
        self.epoch = time()
        self.timer.start(10)

    def _on_pause(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.paused_time = self.total_time

    def _on_reset(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.reset_button.setEnabled(False)
        self.current_time = 0
        self.paused_time = 0
        self.total_time = 0
        self.display_label.setText("00:00.00")

    def show_time(self):
        self.current_time = time() - self.epoch
        self.total_time = self.current_time + self.paused_time
        self.display_label.setText(f"{self.total_time:.2f}")
