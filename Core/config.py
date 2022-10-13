import json 
import os
import sys
import glob
import serial

examIds = {
27:	"تآذر ذراعين",
30:	"إدراك عمق",
31:	"ثبات اليد",
35	:"شدة السمع",
37:	"قبضة يمين",
39:	"الظهر و الرجلين",
40:	"بذل الجهد",
46:	"قبضة شمال",
47:	"الطول",
48:	"الوزن"
}

BASE_URL = "https://192.168.8.1:3000/api/"

BASE_COM_PORT = 3


if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

config_path = application_path + "app.config"

def saveConfigFile(url  , com_port , examid ) : 
   jsonObj = {"url":url, "port" : com_port, "examId":examid}
   with open(config_path, "w") as outfile:
      json.dump(jsonObj, outfile)
   
def getConfigFile():
   # JSON file
   f = open (config_path, "r")
  
   # Reading from file
   config = json.loads(f.read())
   return config



def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
