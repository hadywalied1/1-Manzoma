import sys
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtWidgets import (QMainWindow,
                               QPushButton, QWidget, QLabel,
                               QHBoxLayout, QVBoxLayout, QCheckBox,
                               QProgressBar, QListWidget, QListWidgetItem,
                               QTextEdit,QComboBox )
from PySide2.QtGui import QFont, QIcon
from PySide2.QtCore import Qt
from Core.config import *

import pathlib as path

class Settings(QWidget):
    def __init__(self):
      super(Settings, self).__init__()

      self.layout = QVBoxLayout()
      self.layout.setAlignment(Qt.AlignRight | Qt.AlignAbsolute)
      self.urlEdit = QTextEdit()
      self.urlEdit.setPlaceholderText("enter Address")
      self.urlEdit.setMaximumHeight(100)               
      self.layout.addWidget(self.urlEdit)
      
      self.comEdit = QComboBox()
      self.comEdit.addItems(serial_ports())
      self.comEdit.setMaximumHeight(50)               
      self.layout.addWidget(self.comEdit)
      
        
      self.listWidget = QListWidget()
      items = list(examIds.values())
      for item_text in items:
         item = QListWidgetItem(item_text)
         self.listWidget.addItem(item)
      self.config = getConfigFile() 
      idx = list(examIds.keys()).index(self.config['examId']) 
      item = self.listWidget.item(idx)
      self.listWidget.setCurrentItem(item)
      self.layout.addWidget(self.listWidget)
        
      self.bSubmit = QPushButton("حفظ")
      self.bSubmit.clicked.connect(lambda: self._callback())
      self.layout.addWidget(self.bSubmit)
        
      self.setLayout(self.layout)
        
   
    def _callback(self):
      url = self.urlEdit.toPlainText()
      com = self.comEdit.itemText(self.comEdit.currentIndex())
      data = self.listWidget.currentItem().text()
      examid = list(examIds.keys())[list(examIds.values()).index(data)]
      saveConfigFile(url, com, examid)

