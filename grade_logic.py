from PyQt6.QtWidgets import QMainWindow
from gui import *
import csv
class Grades(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.score1_label.hide()
        self.score2_label.hide()
        self.score3_label.hide()
        self.score4_label.hide()

        self.score1_entry.hide()
        self.score2_entry.hide()
        self.score3_entry.hide()
        self.score4_entry.hide()


