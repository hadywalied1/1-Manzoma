import sys
from PySide2 import QtGui, QtCore,QtWidgets
from PySide2.QtWidgets import (QMainWindow,
                               QPushButton, QWidget, QLabel,
                               QHBoxLayout, QVBoxLayout, QCheckBox,
                               QProgressBar, QListWidget, QListWidgetItem,
                               QTextEdit, )
from PySide2.QtGui import QFont, QIcon
from PySide2.QtCore import Qt


import pathlib as path

from Core.config import getConfigFile

from Core.NetworkReqs import *

class EffortWindow(QWidget):
    ended = QtCore.Signal(object)
        
    def __init__(self, id):
        super(EffortWindow, self).__init__()
        self.setMaximumSize(800,800)
        self.c = 0
        self.id = id
        self.weights = []
        self.lengths = []
        self.weight_median = 0
        self.height_median = 0
        self.config = getConfigFile()
        
        self.weightLayout = QHBoxLayout()
        self.weightLayout.setDirection(QtWidgets.QBoxLayout.Direction.RightToLeft)
        
        self.layout = QVBoxLayout()
        self.Title = QLabel('إختيار بذل الجهد')
        self.Title.setMargin(20)
        self.Title.setAlignment(Qt.AlignHCenter)
        self.Title.setFont(QFont('Arial', 32, QFont.DemiBold))
        self.layout.addWidget(self.Title)
        
        self.instrWidget = QWidget()
        self.instrLayout = QVBoxLayout()
        self.instr = QLabel()
        instructions = """
                    تعليمات الإختبار\n
                \n
                    1- قم بعمل التمرينات لمدة 60 ثانية \n
                    2- ادخل معدل ضربات القلب بعد التمرين\n
                    
                \n
        """
        self.instr.setText(instructions)
        self.instr.setMargin(20)
        
        self.instr.setAlignment(Qt.AlignRight)
        self.instr.setFont(QFont('Arial', 32, QFont.DemiBold))
        self.instrLayout.addWidget(self.instr)
        self.bStartTest = QPushButton("إبدأ الإختبار")
        self.bStartTest.clicked.connect(self.startTest)
        self.instrLayout.addWidget(self.bStartTest)
        
        self.instrWidget.setLayout(self.instrLayout)
        self.layout.addWidget(self.instrWidget)
        
        self.examWidget = QWidget()
        self.examLayout = QVBoxLayout()
        
        self.effortTitle = QLabel("معدل ضربات القلب")
        self.effort = QTextEdit()
        self.effort.setPlaceholderText("معدل ضربات القلب")
        self.effort.setAlignment(Qt.AlignAbsolute | Qt.AlignCenter)
        self.effort.setMaximumHeight(50)
        
        self.examLayout.addWidget(self.effortTitle)
        self.examLayout.addWidget(self.effort)
        
        
        self.bEndTest = QPushButton("إنهاء الإختبار")
        self.bEndTest.clicked.connect(self.sendResult)
        self.examLayout.addWidget(self.bEndTest)
        
        self.examWidget.setLayout(self.examLayout)
        self.examWidget.hide()
        
        self.weightLayout.addLayout(self.layout)
        self.weightLayout.addWidget(self.examWidget)
              
        self.setLayout(self.weightLayout)
        
        
    def startTest(self):
        self.examWidget.show()
        self.bStartTest.hide()

                    
    def sendResult(self):
        result = self.effort.toPlainText()
        req1 = NetworkingAPI("save", {"id":self.id, "examId":40,
                                      "result":result}, index=40000)
        req1.rs.connect(self.endTest)
        req1.start()
        
        
    def endTest(self, txt):
        if(txt != "Error") :
            self.ended.emit(True)
        else :
            pass
            # TODO show error message
   



