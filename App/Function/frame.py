# GUI imports
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout

grid = QGridLayout()

def frame1():
    label = QLabel()
    label.setText("test")
    grid.addWidget(label)