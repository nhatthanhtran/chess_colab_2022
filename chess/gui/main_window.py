from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class ChessMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("What else could it be?")
        uic.loadUi("MainWindow.ui", self)
