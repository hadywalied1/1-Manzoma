import sys, os, logging, faulthandler
from PySide2.QtWidgets import QApplication
from qt_material import apply_stylesheet

from GUI.user_login import LoginWindow
from GUI.MainWindow import MainWindow
from Core.config import *
from Core.EmittingStream import *
import pathlib

logging.basicConfig(level=logging.DEBUG)
faulthandler.is_enabled()
os.environ["PYTHONFAULTHANDLER"] = '1'
os.environ["PYTHONASYNCIODEBUG"] = '0'
os.environ["QT_SCREEN_SCALE_FACTORS"] = '1'
os.environ["QT_SCALE_FACTOR"] = '1'
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = '0'

if(not pathlib.Path(config_path).exists()):
   saveConfigFile(BASE_URL, BASE_COM_PORT, 27)
   
app = QApplication(sys.argv)
app.setApplicationDisplayName("إختبارات العملي و البدني")

apply_stylesheet(app, 'dark_amber.xml')

form = MainWindow()
form.show()

sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
