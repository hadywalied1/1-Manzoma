from PySide2 import QtCore

class EmittingStream(QtCore.QObject):
    textWritten = QtCore.Signal(str)

    def __init__(self, textWrittenFunction):
        QtCore.QObject.__init__(self)
        self.textWritten.connect(textWrittenFunction)

    def write(self, text):
        self.textWritten.emit(str(text))