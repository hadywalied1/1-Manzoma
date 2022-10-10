import sys, os, logging, faulthandler
from PySide2.QtWidgets import QApplication
from qt_material import apply_stylesheet

from GUI.user_login import LoginWindow


logging.basicConfig(level=logging.DEBUG)
faulthandler.is_enabled()
os.environ["PYTHONFAULTHANDLER"] = '1'
os.environ["PYTHONASYNCIODEBUG"] = '0'
os.environ["QT_SCREEN_SCALE_FACTORS"] = '1'
os.environ["QT_SCALE_FACTOR"] = '1'
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = '0'


app = QApplication(sys.argv)
app.setApplicationDisplayName("إختبارات العملي و البدني")

apply_stylesheet(app, 'dark_purple.xml')

form = LoginWindow()
form.show()

sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
