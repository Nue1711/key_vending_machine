from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from utils.write_log import writeExceptionToFile


class LoginController(QObject):
    def __init__(self, user):
        super().__init__()
        self.__user = user
        pass