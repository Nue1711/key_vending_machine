from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QTimer
from utils.write_log import writeExceptionToFile
import socketio 
import datetime

class MainController(QObject):

    def __init__(self):
        super().__init__()
        pass
