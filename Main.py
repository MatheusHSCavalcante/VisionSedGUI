import sys
from VisionSedGUI import *
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import warnings

warnings.simplefilter('ignore', UserWarning)
app = QApplication(sys.argv)
main_window = MyMainWindow()
main_window.show()
sys.exit(app.exec())