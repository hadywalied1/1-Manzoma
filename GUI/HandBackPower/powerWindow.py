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

class PowerWindow(QWidget):
    ended = QtCore.Signal(object)
    
    def __init__(self, id):
        super(PowerWindow, self).__init__()
        self.id = id
        self.setMaximumSize(800,800)
        self.c = 0
        self.config = getConfigFile()
        
        self.powerLayout = QHBoxLayout()
        self.powerLayout.setDirection(QtWidgets.QBoxLayout.Direction.RightToLeft)
        
        self.layout = QVBoxLayout()
        self.Title = QLabel('إختيار قوة القبضة و الظهر  و القدمين')
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
                    1- قم بالوقوف بوضع انتباه و ارفع الذراع الأيمن \n
                    2- أمسك بالقبضة  باليد اليمني ثم اضغط عليها\n
                    3- كرر مع اليد اليسري\n
                    4- كرر مع كلا اليدين علي قبضة الظهر مع التركيز علي الرفع بالظهر والقدمين\n
                    
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
        
        self.leftHandTitle = QLabel("قوة القبضة اليسري")
        self.left = QTextEdit()
        self.left.setPlaceholderText("قوة القبضة اليسري")
        self.left.setAlignment(Qt.AlignAbsolute | Qt.AlignCenter)
   
        
        self.examLayout.addWidget(self.leftHandTitle)
        self.examLayout.addWidget(self.left)
        
        
        self.rightHandTitle = QLabel("قوة القبضة اليمني")
        self.right = QTextEdit()
        self.right.setPlaceholderText("قوة القبضة اليمني")
        self.right.setAlignment(Qt.AlignAbsolute | Qt.AlignCenter)
   
        
        self.examLayout.addWidget(self.rightHandTitle)
        self.examLayout.addWidget(self.right)
        
        
        self.backTitle = QLabel("قوة الظهر و القدمين")
        self.back = QTextEdit()
        self.back.setPlaceholderText("قوة الظهر و القدمين")
        self.back.setAlignment(Qt.AlignAbsolute | Qt.AlignCenter)
        
        
        self.examLayout.addWidget(self.backTitle)
        self.examLayout.addWidget(self.back)
        
        
        self.bEndTest = QPushButton("إنهاء الإختبار")
        self.bEndTest.clicked.connect(self.sendResult)
        self.examLayout.addWidget(self.bEndTest)
        
        self.examWidget.setLayout(self.examLayout)
        self.examWidget.hide()
        self.exaL = QVBoxLayout()
        self.exaL.addWidget(self.examWidget)
        
        self.powerLayout.addLayout(self.layout,3)
        self.powerLayout.addLayout(self.exaL,1)
              
        self.setLayout(self.powerLayout)
        
        
    def startTest(self):
        self.examWidget.show()
        self.bStartTest.hide()

                    
    def sendResult(self):
        result1 = self.left.toPlainText()
        req1 = NetworkingAPI("save", {"id":self.id,
                                      "examId":46,
                                      "result":result1}, index=40000)
        req1.rs.connect(self.endTest)
        req1.start()
        
        result2 = self.right.toPlainText()
        req2 = NetworkingAPI("save", {"id":self.id, "examId":37,
                                      "result":result2}, index=40000)
        req2.rs.connect(self.endTest)
        req2.start()
        
        result3 = self.back.toPlainText()
        req3 = NetworkingAPI("save", {"id":self.id, "examId":39,
                                      "result":result3}, index=40000)
        req3.rs.connect(self.endTest)
        req3.start()
        
        
    def endTest(self, txt):
        if(txt != "Error") :
            self.c = self.c+1
            if self.c == 3 :
                self.ended.emit(True)
        else:
            pass
            # TODO show error message
        

