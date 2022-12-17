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

class ArmsWindow(QWidget):
    ended = QtCore.Signal(object)
    
    def __init__(self, id):
      pass
#         super(ArmsWindow, self).__init__()
#         self.setMaximumSize(800,800)
#         self.c = 0
#         self.requiredTries = 1
#         self.id = id
#         self.depths = []
#         self.depth_median = 0
#         self.depthData = 0
#         self.config = getConfigFile()
#         self.serialThread = EmittingStream(index=2000)
#         self.serialThread.rs.connect(self.setData)    
#         self.serialThread.deviceConnection.connect(self.testFinished)    
        
#         self.depthLayout = QHBoxLayout()
#         self.depthLayout.setDirection(QtWidgets.QBoxLayout.Direction.RightToLeft)
        
#         self.layout = QVBoxLayout()
#         self.Title = QLabel('إختيار تآذر الذراعين')
#         self.Title.setProperty('class', 'center')
#         self.Title.setMargin(20)
#         self.Title.setAlignment(Qt.AlignHCenter)
#         self.Title.setFont(QFont('Arial', 32, QFont.DemiBold))
#         self.layout.addWidget(self.Title)
        
#         self.testTitle = QLabel('الإختبار التجريبي')
#         self.testTitle.setMargin(20)
#         self.testTitle.setAlignment(Qt.AlignHCenter)
#         self.testTitle.setFont(QFont('Arial', 32, QFont.DemiBold))
#         self.layout.addWidget(self.testTitle)
        
#         self.instrWidget = QWidget()
#         self.instrLayout = QVBoxLayout()
#         self.instr = QLabel()
#         self.instr.setProperty('class', 'just')
#         instructions = """
#                     تعليمات الإختبار\n
#                 \n
#                     1- مر علي النجمة بواسطةالمقبضين \n
#                 \n
#         """
#         self.instr.setText(instructions)
#         self.instr.setMargin(20)
#         self.instr.setAlignment(Qt.AlignRight)
#         self.instr.setFont(QFont('Arial', 32, QFont.DemiBold))
#         self.instrLayout.addWidget(self.instr)

#         self.bStartTest = QPushButton(" إبدأ الإختبار التجريبي")
#         self.bStartTest.clicked.connect(self.startTest)
#         self.instrLayout.addWidget(self.bStartTest)
                
#         self.instrWidget.setLayout(self.instrLayout)
#         self.layout.addWidget(self.instrWidget)
        
#         self.examWidget = QWidget()
#         self.examLayout = QVBoxLayout()
        
#         self.depthTitle = QLabel("المسافة")
#         self.depthLine = QLineEdit()
#         self.depthLine.setDisabled(True)
#         self.depthLine.setPlaceholderText("المسافة")
#         self.depthLine.setAlignment(Qt.AlignAbsolute | Qt.AlignCenter)
#         self.depthLine.setMaximumHeight(50)
        
#         self.examLayout.addWidget(self.depthTitle)
#         self.examLayout.addWidget(self.depthLine)
        
#         self.depthResult = QLabel("Result :")
#         self.depthResult.hide()
#         self.examLayout.addWidget(self.depthResult)

        
#         self.bEndTest = QPushButton("بدء الإختبار")
#         self.bEndTest.clicked.connect(self.sendResult)
#         self.bEndTest.setDisabled(True)
#         self.examLayout.addWidget(self.bEndTest)
        
#         self.examWidget.setLayout(self.examLayout)
#         self.examWidget.hide()
        
#         self.depthLayout.addLayout(self.layout,2)
#         self.depthLayout.addWidget(self.examWidget)
              
#         self.setLayout(self.depthLayout)
        
        
#     def startTest(self):
#         self.examWidget.show()
#         self.serialThread.start()
#         self.bStartTest.hide()

    
#     def testFinished(self, t):
#         if(not t):
#             self.bEndTest.setDisabled(False)
#             self.serialThread.stop()
        
#     def setData(self, txt):
#         d = txt.split(",")
#         if d[0] == "LABEL":
#             return
#         depth = d[-3].strip()
#         self.depthData = d[-1].strip()
#         res = "النتيجة : " + str (self.depthData)
#         self.depthResult.setText(res)
#         self.depths.append(round(float(depth),1))
#         self.depth_median = round(NP.median(NP.array(self.depths)))
#         self.depthLine.setText(str(self.depth_median))
                    
#     def sendResult(self):
#         if self.c == self.requiredTries:
#             self.serialThread.stop()
#             req1 = NetworkingAPI("save", {"id":self.id, "examId":30,
#                                         "result":self.depthData}, index=1)
#             req1.rs.connect(self.endTest)
#             req1.start()
#         elif self.c == self.requiredTries - 1:
#             self.serialThread.start()
#             if self.c == 0 :
#                 self.depths = []
#                 self.depth_median = 0
#                 self.depthData = 0
#             self.depthLine.clear()
#             self.bStartTest.setText("الإختبار")
#             self.bEndTest.setText("إنهاء الإختبار")
#             res = "النتيجة : " + str (self.depthData)
#             self.depthResult.setText(res)
#             self.depthResult.show()
#             self.c = self.c + 1
#         else :
#             self.serialThread.start()
#             self.depthLine.clear()
#             self.c = self.c + 1    
        
        
#     def endTest(self, txt):
#         if(txt != "Error") :
#             self.ended.emit(True)
   


