import sys
from PySide2 import QtGui, QtCore
from PySide2.QtWidgets import (QMainWindow,
                               QPushButton, QWidget, QLabel,
                               QHBoxLayout, QVBoxLayout, QCheckBox,
                               QProgressBar, QListWidget, QListWidgetItem,
                               QTextEdit, )
from PySide2.QtGui import QFont, QIcon
from PySide2.QtCore import Qt


import pathlib as path
from Core.config import *

class DepthWindow(QWidget):
    ended = QtCore.Signal(object)
    
    def __init__(self, id):
        self.id = id
        pass
   
    def show():
        pass

