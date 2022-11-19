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
import winsound

from Core.config import *
from Core.EmittingStream import *

from Core.NetworkReqs import NetworkingAPI

import numpy as NP

from Core.EmittingStream import *
from Core.NetworkReqs import NetworkingAPI

class WeightWindow(QWidget):
    ended = QtCore.Signal(object)
    
    def __init__(self, id):
        super(WeightWindow, self).__init__()
        self.setMaximumSize(800,800)
        self.c = 0
        self.id = id
        self.weights = []
        self.lengths = []
        self.weight_median = 0
        self.height_median = 0
        self.config = getConfigFile()
        self.serialThread = EmittingStream(index=2000)
        self.serialThread.rs.connect(self.setData)    
        self.serialThread.deviceConnection.connect(self.testFinished)    
        
        self.weightLayout = QHBoxLayout()
        self.weightLayout.setDirection(QtWidgets.QBoxLayout.Direction.RightToLeft)
        
        self.layout = QVBoxLayout()
        self.Title = QLabel('إختيار الطول و الوزن')
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
                    2- عند سماع الصافرة الأولي اصعد علي الميزان\n
                    3- انتظر سماع الصافرة الثانية\n
                    4- عند سماع الصافرة الثانية انزل من علي الميزان\n
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
        self.weight = QTextEdit()
        self.weight.setDisabled(True)
        self.weight.setPlaceholderText("الوزن")
        self.weight.setAlignment(Qt.AlignAbsolute | Qt.AlignCenter)
        self.weight.setMaximumHeight(50)
        
        self.examLayout.addWidget(self.weightTitle)
        self.examLayout.addWidget(self.weight)
        
        self.lengthTitle = QLabel("الطول")
        self.length = QTextEdit()
        self.length.setDisabled(True)
        self.length.setPlaceholderText("الطول")
        self.length.setAlignment(Qt.AlignAbsolute | Qt.AlignCenter)
        self.length.setMaximumHeight(50)
        
        self.examLayout.addWidget(self.lengthTitle)
        self.examLayout.addWidget(self.length)
        
        self.bEndTest = QPushButton("إنهاء الإختبار")
        self.bEndTest.clicked.connect(self.sendResult)
        self.bEndTest.setDisabled(True)
        self.examLayout.addWidget(self.bEndTest)
        
        self.examWidget.setLayout(self.examLayout)
        self.examWidget.hide()
        
        self.weightLayout.addLayout(self.layout)
        self.weightLayout.addWidget(self.examWidget)
              
        self.setLayout(self.weightLayout)
        
        
    def startTest(self):
        self.examWidget.show()
        self.serialThread.start()
        self.bStartTest.hide()
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
    
    def restartTest(self):
        self.bEndTest.setDisabled(True)
        self.bRestart.setDisabled(True)
        self.serialThread.start()
        self.bStartTest.hide()
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
    
    def testFinished(self, t):
        if(not t):
            frequency = 1500  # Set Frequency To 1500 Hertz
            duration = 1000  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
            self.bEndTest.setDisabled(False)
            self.bRestart.setDisabled(False)
            self.bRestart.show()
            self.serialThread.stop()
        
    def setData(self, txt):
        d = txt.split(",")
        
        weight = d[1].strip()
        if float(weight) > 30.0:
                self.weights.append(round(float(weight),2))
        
        length = d[2].strip()
        if float(length) > 60.0:
                self.lengths.append(round(float(length),1))
        self.weight_median = round(NP.max(NP.array(self.weights)))
        self.height_median = round(NP.max(NP.array(self.lengths))) 
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
   

