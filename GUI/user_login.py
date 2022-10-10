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


class LoginWindow(QMainWindow):
  def __init__(self):
    super(LoginWindow, self).__init__()
    self.setWindowTitle("AFTC")

    self.layout = QVBoxLayout()
    self.Title = QLabel('من فضلك قم بإدخال الرقم العسكري/الرقم الثلاثي/ الرقم القومي للممتحن و اختيار الإختبار \n ثم إضغط علي بحث')
    self.Title.setMargin(20)
    self.Title.setAlignment(Qt.AlignHCenter)
    self.Title.setFont(QFont('Arial', 32, QFont.DemiBold))
    self.layout.addWidget(self.Title)
    
    self.number = QTextEdit()
    self.number.setPlaceholderText("قم بإدخال الرقم العسكري / الرقم  الثلاثي / الرقم القومي")
    self.number.setFont(QFont('Ariel', 48, QFont.DemiBold))
    self.number.setAlignment(Qt.AlignAbsolute | Qt.AlignCenter)
    self.number.setMaximumHeight(75)
    self.layout.addWidget(self.number)
    
    
    self.listWidget = QListWidget()
    items = list(["طول و وزن", "قبضة يد"])
    for item_text in items:
        item = QListWidgetItem(item_text)
        self.listWidget.addItem(item)
    item = self.listWidget.item(0)
    self.listWidget.setCurrentItem(item)
    self.layout.addWidget(self.listWidget)
    
    self.bSubmit = QPushButton("بحث")
    self.layout.addWidget(self.bSubmit)
    
    self.window = QWidget()
    self.window.setLayout(self.layout)
    self.setCentralWidget(self.window)
   


