import sys
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

from GUI.settingsUI import Settings

class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()

        self.config = getConfigFile()

        self.settingsWidget = Settings()

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
        self.layout.addWidget(self.bSubmit)

        self.userdataWidget = QWidget()
        self.userdataLayout = QVBoxLayout()
        self.username = QLabel()
        self.userNumber = QLabel()
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
        self.mainlayout.addWidget(self.examWidget)
        
        self.setLayout(self.mainlayout)
    
    def showSettings(self):
        
        if(self.settingsWidget.isVisible()):
            self.settingsWidget.hide()
        else:
            self.settingsWidget.show()        
    
    def startTesting(self):
        pass
    
    def _callback(self):
        pass

