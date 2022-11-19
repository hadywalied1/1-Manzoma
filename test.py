import sys,os, logging, faulthandler
from PySide2.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QAction, QStatusBar
)
from PySide2 import QtWidgets,QtCore,QtGui
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt
from qt_material import apply_stylesheet
from Core.EmittingStream import EmittingStream




logging.basicConfig(level=logging.ERROR)
faulthandler.is_enabled()
os.environ["PYTHONFAULTHANDLER"] = '1'
os.environ["PYTHONASYNCIODEBUG"] = '0'
os.environ["QT_SCREEN_SCALE_FACTORS"] = '1'
os.environ["QT_SCALE_FACTOR"] = '1'
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = '0'

class ui_Firstwindow(object):
    def nextWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ui_Secondwindow()
        self.ui.setupUi(self.window)
        app.closeAllWindows()
        self.window.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 471)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton.setGeometry(QtCore.QRect(210, 140, 191, 41))
        # self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.nextWindow)
        
        
class ui_Secondwindow(object):
    def previouswindow(self):
        pass
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 650)
        Dialog.setMinimumSize(QtCore.QSize(552, 0))

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 240, 70, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.previouswindow)



class Firstwindow(QtWidgets.QMainWindow, ui_Firstwindow):
    def __init__(self, parent=None):
        super(Firstwindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hide)


class Secondwindow(QtWidgets.QDialog, ui_Secondwindow):
    def __init__(self, parent=None):
        super(Secondwindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.hide)


class Manager:
    def __init__(self):
        self.first = Firstwindow()
        self.second = Secondwindow()

        self.first.pushButton.clicked.connect(self.second.show)
        self.second.pushButton_2.clicked.connect(self.first.show)

        self.first.show()




app = QApplication(sys.argv)
apply_stylesheet(app, 'dark_yellow.xml')
w = Manager()

# try:
#     networkCall = NetworkingAPI(req="examiner", inputs={"id":"29811010109296"})

#     networkCall.rs.connect(lambda text: print(str(text)))
#     networkCall.run()
# finally : 
#     networkCall.stop()
    
e = EmittingStream(index=1000)
e.rs.connect(lambda text: print(str(text)))
e.start()

app.exec_()
