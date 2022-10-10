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

class EmittingStream(QtCore.QObject):
    textWritten = QtCore.Signal(str)

    def __init__(self, textWrittenFunction):
        QtCore.QObject.__init__(self)
        self.textWritten.connect(textWrittenFunction)

    def write(self, text):
        self.textWritten.emit(str(text))


class EffortWindow(QMainWindow):
  def __init__(self):
      pass
   
  def show():
      pass

