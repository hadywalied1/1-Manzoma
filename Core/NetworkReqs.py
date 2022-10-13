from PySide2 import QtCore, QtGui, QtNetwork
import sys
from config import *
from EmittingStream import EmittingStream
      
      
class NetworkingAPI:
  
    def __init__(self, responseCallback):    
      self.responseCallback = responseCallback
      self.emittingStream = EmittingStream(self.responseCallback)
      
      
    def getExaminer(self,id):
      url = QtCore.QUrl(BASE_URL)
      query = QtCore.QUrlQuery(url)
      query.addQueryItem("id", id)
      url.setQuery(query)
      req = QtNetwork.QNetworkRequest(url)
      self.nam = QtNetwork.QNetworkAccessManager()
      self.nam.finished.connect(self.handleResponse)
      self.nam.get(req)    

    def checkIsDone(self,id,examId):
      url = QtCore.QUrl(BASE_URL)
      query = QtCore.QUrlQuery(url)
      query.addQueryItem("id", id)
      query.addQueryItem("examId", examId)
      url.setQuery(query)
      req = QtNetwork.QNetworkRequest(url)
      self.nam = QtNetwork.QNetworkAccessManager()
      self.nam.finished.connect(self.handleResponse)
      self.nam.get(req)    

    def saveExam(self,id,examId, result):
      url = QtCore.QUrl(BASE_URL)
      query = QtCore.QUrlQuery(url)
      query.addQueryItem("id", id)
      query.addQueryItem("examId", examId)
      query.addQueryItem("result", result)
      url.setQuery(query)
      req = QtNetwork.QNetworkRequest(url)
      self.nam = QtNetwork.QNetworkAccessManager()
      self.nam.finished.connect(self.handleResponse)
      self.nam.post(req) 

         
    def handleResponse(self, reply):
      er = reply.error()
      if er == QtNetwork.QNetworkReply.NoError:
         bytes_string = reply.readAll()
         print(str(bytes_string, 'utf-8'))
         self.emittingStream.write(str(bytes_string,'utf-8'))
      else:
         print("Error occured: ", er)
         print(reply.errorString())
         self.emittingStream.write("Error")            