import sys
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtWidgets import (QMainWindow,
                               QPushButton, QWidget, QLabel,
                               QHBoxLayout, QVBoxLayout, QCheckBox,
                               QProgressBar, QListWidget, QListWidgetItem,
                               QTextEdit, )
from PySide2.QtGui import QFont, QIcon
from PySide2.QtCore import Qt


import pathlib as path

from GUI.user_login import LoginWindow
from GUI.settingsUI import Settings


class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.setWindowTitle("AFTC")
    self.setMaximumSize(800,800)
    self.mainlayout = QHBoxLayout()
    self.mainlayout.setDirection(QtWidgets.QBoxLayout.Direction.RightToLeft)
    self.w = LoginWindow()
    self.mainlayout.addWidget(self.w)
    self.window = QWidget()
    self.window.setLayout(self.mainlayout)
    self.setCentralWidget(self.window)
   


