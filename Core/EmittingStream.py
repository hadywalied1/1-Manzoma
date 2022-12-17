from PySide2 import QtCore
 
from serial import *
from Core.config import *

class EmittingStream(QtCore.QThread):
    rs = QtCore.Signal(object)
    deviceConnection = QtCore.Signal(object)
    
    def __init__(self, parent = None, index =1998):
        super(EmittingStream, self).__init__(parent)
        self.config  = getConfigFile()    
        self.index = index
        self.is_running = True
                       

    def write(self, text):
        self.rs.emit(str(text))
    
    
    def conn(self):
        i=0
        while i<10:
            try:
                self.serial = Serial(self.config['port'], 9600,
                                     timeout=0.1)
                self.deviceConnection.emit(True)
                break
            except Exception as e:
                print(e)
                self.deviceConnection.emit(False)
                print("reconnecting....")
                self.sleep(500)
                i=i+1
                if i==9:
                    print("failed to connect...")
   
    def readLines(self):
        start = int(time.time())
        while int(time.time()) - start < 10:
            line = self.serial.readline()
            if(line):
                line = line.decode('UTF-8')
                self.write(str(line))
                print(line)
        self.deviceConnection.emit(False)
        # self.stop()
            
    def run(self):
        print('Starting thread...', self.index)
        try:
            self.conn()
            self.readLines()
        except Exception as e:
            print(e)
            

    def stop(self):
        self.is_running = False
        self.serial.close()
        # self.deviceConnection.emit(False)
        print('Stopping thread...', self.index)
        self.terminate()

