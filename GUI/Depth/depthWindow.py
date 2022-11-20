import sys
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtWidgets import (QMainWindow,
                               QPushButton, QWidget, QLabel,
                               QHBoxLayout, QVBoxLayout, QCheckBox,
                               QProgressBar, QListWidget, QListWidgetItem,
                               QTextEdit, QLineEdit, )
from PySide2.QtGui import QFont, QIcon
from PySide2.QtCore import Qt

import pathlib as path


from Core.config import *
from Core.EmittingStream import *

from Core.NetworkReqs import NetworkingAPI

import numpy as NP

from Core.EmittingStream import *
from Core.NetworkReqs import NetworkingAPI


class DepthWindow(QWidget):
    ended = QtCore.Signal(object)
    
    def __init__(self, id):
        super(DepthWindow, self).__init__()
        self.setMaximumSize(800,800)
        self.c = 0
        self.id = id
        self.depths = []
        self.depth_median = 0
        self.config = getConfigFile()
        self.serialThread = EmittingStream(index=2000)
        self.serialThread.rs.connect(self.setData)    
        self.serialThread.deviceConnection.connect(self.testFinished)    
        
        self.depthLayout = QHBoxLayout()
        self.depthLayout.setDirection(QtWidgets.QBoxLayout.Direction.RightToLeft)
        
        self.layout = QVBoxLayout()
        self.Title = QLabel('إختيار ادراك العمق')
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
                    1- إنتظر سماع صوت الصافرة الأولي \n
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
        self.bRestart = QPushButton("إعادة قياس")
        self.bRestart.clicked.connect(self.restartTest)
        self.bRestart.hide()
        self.instrLayout.addWidget(self.bRestart)
        
        self.instrWidget.setLayout(self.instrLayout)
        self.layout.addWidget(self.instrWidget)
        
        self.examWidget = QWidget()
        self.examLayout = QVBoxLayout()
        
        self.weightTitle = QLabel("الوزن")
        self.weight = QLineEdit()
        self.weight.setDisabled(True)
        self.weight.setPlaceholderText("الوزن")
        self.weight.setAlignment(Qt.AlignAbsolute | Qt.AlignCenter)
        self.weight.setMaximumHeight(50)
        
        self.examLayout.addWidget(self.weightTitle)
        self.examLayout.addWidget(self.weight)

        
        self.bEndTest = QPushButton("إنهاء الإختبار")
        self.bEndTest.clicked.connect(self.sendResult)
        self.bEndTest.setDisabled(True)
        self.examLayout.addWidget(self.bEndTest)
        
        self.examWidget.setLayout(self.examLayout)
        self.examWidget.hide()
        
        self.depthLayout.addLayout(self.layout)
        self.depthLayout.addWidget(self.examWidget)
              
        self.setLayout(self.depthLayout)
        
        
    def startTest(self):
        self.examWidget.show()
        self.serialThread.start()
        self.bStartTest.hide()

    
    def restartTest(self):
        self.bEndTest.setDisabled(True)
        self.bRestart.setDisabled(True)
        self.serialThread.start()
        self.bStartTest.hide()

    
    def testFinished(self, t):
        if(not t):
            self.bEndTest.setDisabled(False)
            self.bRestart.setDisabled(False)
            self.serialThread.stop()
        
    def setData(self, txt):
        d = txt.split(",")
        
        weight = d[1].strip()
        if float(weight) > 30.0:
                self.depths.append(round(float(weight),2))
        
        
        self.depth_median = round(NP.max(NP.array(self.weights)))
         
        self.weight.setText(str(self.weight_median))
        self.length.setText(str(self.height_median))
                    
    def sendResult(self):
        self.serialThread.stop()
        req1 = NetworkingAPI("save", {"id":self.id, "examId":47,
                                      "result":self.height_median}, index=1)
        req1.rs.connect(self.endTest)
        req1.start()
        req2 = NetworkingAPI("save", {"id":self.id, "examId":48,
                                      "result":self.weight_median}, index=2)
        req2.rs.connect(self.endTest)
        req2.start()
        
    def endTest(self, txt):
        if(txt != "Error") :
            self.c = self.c+1
        if self.c == 2 :
            self.ended.emit(True)
   

