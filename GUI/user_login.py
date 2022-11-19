import sys
from GUI.Weight.weight_window import WeightWindow
from GUI.Arms.armsWindow import ArmsWindow
from GUI.Depth.depthWindow import DepthWindow
from GUI.Effort.effort_window import EffortWindow
from GUI.HandStability.stabilityWindow import StabilityWindow
from GUI.HandBackPower.powerWindow import PowerWindow
from GUI.Hearing.hearingWindow import HearingWindow

from PySide2 import QtGui, QtCore,QtWidgets
from PySide2.QtWidgets import (QMainWindow,QLineEdit,
                               QPushButton, QWidget, QLabel,
                               QHBoxLayout, QVBoxLayout, QCheckBox,
                               QProgressBar, QListWidget, QListWidgetItem,
                               QTextEdit, )
from PySide2.QtGui import QFont, QIcon
from PySide2.QtCore import Qt


import pathlib as path
from Core.config import *
from Core.NetworkReqs import NetworkingAPI

from GUI.settingsUI import Settings

class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()

        self.config = getConfigFile()

        self.settingsWidget = Settings()
        self.settingsWidget.saved.connect(self.config_changed)
        self.mainlayout = QHBoxLayout()
        self.mainlayout.setDirection(QtWidgets.QBoxLayout.Direction.RightToLeft)
        
        self.layout = QVBoxLayout()
        
        self.settingsLabel = QLabel("")
        self.settingsBtn = QPushButton("الإعدادات")
        self.settingsBtn.clicked.connect(self.showSettings)
        self.settingsLayout = QHBoxLayout()
        self.settingsLayout.addWidget(self.settingsLabel,6)
        self.settingsLayout.addWidget(self.settingsBtn,1)
        self.layout.addLayout(self.settingsLayout)
        
        self.Title = QLabel('من فضلك قم بإدخال الرقم العسكري/الرقم الثلاثي/ الرقم القومي للممتحن و اختيار الإختبار \n ثم إضغط علي بحث')
        self.Title.setMargin(20)
        self.Title.setAlignment(Qt.AlignHCenter)
        self.Title.setFont(QFont('Arial', 32, QFont.DemiBold))
        self.layout.addWidget(self.Title)
        
        self.number = QLineEdit()
        self.number.setPlaceholderText("قم بإدخال الرقم العسكري / الرقم  الثلاثي / الرقم القومي")
        self.number.setClearButtonEnabled(True)
        self.number.setAlignment(Qt.AlignAbsolute | Qt.AlignCenter)
        self.layout.addWidget(self.number)
        
        
        self.bSubmit = QPushButton("بحث")
        self.bSubmit.clicked.connect(self.searchUser)
        self.layout.addWidget(self.bSubmit)

        self.progress = QProgressBar()
        self.progress.setMinimum(0)
        self.progress.setMaximum(0)
        self.progress.hide()
        self.layout.addWidget(self.progress)
        
        self.userdataWidget = QWidget()
        self.userdataLayout = QVBoxLayout()
        self.username = QLabel("username")
        self.userNumber = QLabel("user number")
        self.examName = QLabel("إسم الإختبار : " + examIds[self.config['examId']])
        self.startTest = QPushButton("إبدأ الإختبار")
        self.startTest.clicked.connect(self.startTesting)
        self.userdataLayout.addWidget(self.username)
        self.userdataLayout.addWidget(self.userNumber)
        self.userdataLayout.addWidget(self.examName)
        self.userdataLayout.addWidget(self.startTest)
        self.userdataWidget.setLayout(self.userdataLayout)
        self.userdataWidget.hide()
        self.layout.addWidget(self.userdataWidget)
        
        self.layout.setSpacing(30)
        self.mainlayout.addLayout(self.layout)
        
                
        self.examWidget = QWidget()
        self.examWidget.hide()
        # self.mainlayout.addWidget(self.examWidget)
        
        self.setLayout(self.mainlayout)
    
    def showSettings(self):
        if(self.settingsWidget.isVisible()):
            self.settingsWidget.hide()
        else:
            self.settingsWidget.show()        
    
    def searchUser(self):
        self.progress.show()
        try:
            networkCall = NetworkingAPI(req="examiner", inputs={"id":self.number.text()}, index = 100)
            networkCall.rs.connect(lambda text: self.userFound(str(text)))
            networkCall.run()
        finally:
            pass
            # networkCall.stop()
        
    def userFound(self, text):
        self.progress.hide()
        self.userdataWidget.show()
        s = json.loads(text)
        self.username.setText("الإسم: " + s["name"])
        self.userNumber.setText("الرقم العسكري : "+s["sold_id"])
        
    
    def startTesting(self):
        try:
            self.progress.show()
            networkCall = NetworkingAPI(req="check", inputs={"id":self.number.text(),
                                                            "examId" : str(self.config["examId"])}, index=110)
            networkCall.rs.connect(lambda text: self.examFound(str(text)))
            networkCall.run()
        finally:
            pass
            # networkCall.stop()        
       
    def examFound(self, text):
        self.progress.hide()
        s = json.loads(text)
        if(s["done"] == 1):
            if self.config["examId"] == 27: #arms
                layout = QVBoxLayout()
                widget = ArmsWindow(self.number.text())
                widget.ended.connect(self.endExam)
                layout.addWidget(widget)
                self.examWidget.setLayout(layout)
            elif self.config["examId"] == 30: #depth
                layout = QVBoxLayout()
                widget = DepthWindow(self.number.text())
                widget.ended.connect(self.endExam)
                layout.addWidget(widget)
                self.examWidget.setLayout(layout)
            elif self.config["examId"] == 31: #stability
                layout = QVBoxLayout()
                widget = StabilityWindow(self.number.text())
                widget.ended.connect(self.endExam)
                layout.addWidget(widget)
                self.examWidget.setLayout(layout)
            elif self.config["examId"] == 35: # hearing
                layout = QVBoxLayout()
                widget = HearingWindow(self.number.text())
                widget.ended.connect(self.endExam)
                layout.addWidget(widget)
                self.examWidget.setLayout(layout)
            elif self.config["examId"] == 37 or self.config["examId"] == 39 \
                or self.config["examId"] == 46: #power
                layout = QVBoxLayout()
                widget = PowerWindow(self.number.text())
                widget.ended.connect(self.endExam)
                layout.addWidget(widget)
                self.examWidget.setLayout(layout)
            elif self.config["examId"] == 40: #effort
                layout = QVBoxLayout()
                widget = EffortWindow(self.number.text())
                widget.ended.connect(self.endExam)
                layout.addWidget(widget)
                self.examWidget.setLayout(layout)
            elif self.config["examId"] == 47 or self.config["examId"] == 48: #weight
                layout = QVBoxLayout()
                widget = WeightWindow(self.number.text())
                widget.ended.connect(self.endExam)
                layout.addWidget(widget)
                self.examWidget.setLayout(layout)
            else :
                print("WTF DUDE")
                
            self.examWidget.show()
        else:
            print("WTF")
    
    def endExam(self):
        self.examWidget.hide()
        self.userdataWidget.hide()
        self.examWidget = QWidget()

        print("exam Ended")
        
    def config_changed(self,tex):
        self.config = getConfigFile()
    

