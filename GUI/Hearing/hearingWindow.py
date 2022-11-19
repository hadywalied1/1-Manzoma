import sys
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtWidgets import (QMainWindow,QComboBox,
                               QPushButton, QWidget, QLabel,
                               QHBoxLayout, QVBoxLayout, QCheckBox,
                               QProgressBar, QListWidget, QListWidgetItem,
                               QTextEdit, )
from PySide2.QtGui import QFont, QIcon
from PySide2.QtCore import Qt


import pathlib as path
from Core.config import getConfigFile

from Core.NetworkReqs import *

class HearingWindow(QWidget):
    ended = QtCore.Signal(object)
    
    def __init__(self, id):
        super(HearingWindow, self).__init__()
        self.setMaximumSize(800,800)
        
        self.id = id
        self.grades = ['500 Hz جيد', '1000 Hz مقبول'] 
        
        self.config = getConfigFile()
        
        self.hearingLayout = QHBoxLayout()
        self.hearingLayout.setDirection(QtWidgets.QBoxLayout.Direction.RightToLeft)
        
        self.mainLayout = QVBoxLayout()
        self.Title = QLabel('إختيار شدة السمع')
        self.Title.setMargin(20)
        self.Title.setAlignment(Qt.AlignHCenter)
        self.Title.setFont(QFont('Arial', 32, QFont.DemiBold))
        self.mainLayout.addWidget(self.Title)
        
        self.instrWidget = QWidget()
        self.instrLayout = QVBoxLayout()
        self.instr = QLabel()
        instructions = """
                    تعليمات الإختبار\n
                \n
                    1- يقف الجندي امام الجهاز و يرتدي السماعة\n
                    2- يتم تشغيل عدة نغمات للجندي علي الأذن اليمني و اليسري\n
                    3- يضغط الجندي علي الزر المرفق بالسماعة و يشير الي الأذن التي سمع عندها الصوت\n
                    4- يكرر الإختبار عند عدة نغمات و ترددات\n
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
        self.mainLayout.addWidget(self.instrWidget)
        
        self.examWidget = QWidget()
        self.examLayout = QVBoxLayout()
        self.examLayout.setContentsMargins(25,25,25,25)
        
        self.comEdit = QComboBox()
        self.comEdit.addItems(self.grades)
        self.comEdit.setMaximumHeight(50)               
        self.examLayout.addWidget(self.comEdit)
      
        self.bEndTest = QPushButton("إنهاء الإختبار")
        self.bEndTest.clicked.connect(self.sendResult)
        # self.bEndTest.setDisabled(True)
        self.examLayout.addWidget(self.bEndTest)
        
        self.examWidget.setLayout(self.examLayout)
        self.examWidget.hide()
        
        self.hearingLayout.addLayout(self.mainLayout)
        self.hearingLayout.addWidget(self.examWidget)
              
        self.setLayout(self.hearingLayout)
        
        
    def startTest(self):
        self.examWidget.show()
        self.bStartTest.hide()

                    
    def sendResult(self):
        result = self.comEdit.currentData()
        req1 = NetworkingAPI("save", {"id":self.id,
                                      "examId":35,
                                      "result":result},
                                    index=35000)
        req1.rs.connect(self.endTest)
        req1.start()
        
        
    def endTest(self, txt):
        if(txt != "Error") :
            self.ended.emit(True)
        else:
            pass #TODO HANDLE ERROR MESSAGES
   



