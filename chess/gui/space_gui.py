from PyQt6.QtCore import QRect
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QWidget
class SpaceGUI(QWidget):
    def __init__(self, int_x_pos, int_y_pos):
        super().__init__()
        # self.qcl_color = QColor(int((int_x_pos + int_y_pos) % 2 == 0))
        self.qcl_color = QColor("black")


if __name__=="main":
    test = SpaceGUI()