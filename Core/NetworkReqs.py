from PySide2 import QtCore, QtGui, QtNetwork
import sys
from Core.config import *
from Core.EmittingStream import EmittingStream
      
      
class NetworkingAPI(QtCore.QThread):
    rs = QtCore.Signal(object)
    
    def __init__(self, req : str, inputs , parent = None, index =0): 
      super(NetworkingAPI, self).__init__(parent)  
      self.config = getConfigFile()
      self.ip = self.config['url']
      self.inputs = inputs
      self.index = index
      self.is_running = True
      if req =="examiner":
        self.func = self.getExaminer
      elif req == "check":
        self.func = self.checkIsDone
      elif req == "save":
        self.func = self.saveExam
      
    def getExaminer(self,id):
      url = QtCore.QUrl(self.ip + '/getExaminer')
      query = QtCore.QUrlQuery(url)
      query.addQueryItem("id", id)
      url.setQuery(query)
      req = QtNetwork.QNetworkRequest(url)
      self.nam = QtNetwork.QNetworkAccessManager()
      self.nam.finished.connect(self.handleResponse)
      self.nam.get(req)    

    def checkIsDone(self,id,examId):
      url = QtCore.QUrl(self.ip + '/checkIsDone')
      query = QtCore.QUrlQuery(url)
      query.addQueryItem("id", id)
      query.addQueryItem("examId", examId)
      url.setQuery(query)
      req = QtNetwork.QNetworkRequest(url)
      self.nam = QtNetwork.QNetworkAccessManager()
      self.nam.finished.connect(self.handleResponse)
      self.nam.get(req)    

    def saveExam(self,id,examId, result):
      url = QtCore.QUrl(self.ip + '/saveExam')
      
      req = QtNetwork.QNetworkRequest(url)
      req.setHeader(QtNetwork.QNetworkRequest.ContentTypeHeader, "application/json")
      obj = {"barcode":str(id), "examid": int(examId), "result": str(result)}
      doc = QtCore.QJsonDocument(obj)
      jobj = doc.toJson()
      self.nam = QtNetwork.QNetworkAccessManager()
      self.nam.finished.connect(self.handleResponse)
      self.nam.post(req, jobj) 

         
    def handleResponse(self, reply):
      er = reply.error()
      if er == QtNetwork.QNetworkReply.NoError:
         bytes_string = reply.readAll()
         print(str(bytes_string, 'utf-8'))
         self.rs.emit(str(bytes_string,'utf-8'))
      else:
         print("Error occured: ", er)
         print(reply.errorString())   
         self.rs.emit("Error")
        
    def run(self):
        print('Starting thread...', self.index)
        try:
            self.func(**self.inputs)
        except Exception as e:
            print(e)

    def stop(self):
        self.is_running = False
        print('Stopping thread...', self.index)
        self.terminate()
