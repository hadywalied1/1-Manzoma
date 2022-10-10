import json 
import os, sys

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