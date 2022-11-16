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
    
    def __init__(self):
        super(DepthWindow, self).__init__()
        
        self.config = getConfigFile()
        self.layout = QVBoxLayout()
        self.Title = QLabel('')
        self.Title.setMargin(20)
        self.Title.setAlignment(Qt.AlignHCenter)
        self.Title.setFont(QFont('Arial', 32, QFont.DemiBold))
        self.layout.addWidget(self.Title)
        self.setLayout(self.layout)
        
   
    def show():
        pass

