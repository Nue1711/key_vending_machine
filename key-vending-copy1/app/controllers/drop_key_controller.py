from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from utils.write_log import writeExceptionToFile
#from controllers.threads.thread_checkin import ThreadCheckin
#from controllers.threads.thread_control_door import ThreadControlDoor
#from utils.observable_trigger import ObservableTrigger
#obs = ObservableTrigger.getInstance()

class DropKeyController(QObject):
    def __init__(self, user):
        super().__init__()
        self.__user = user
        pass
'''
    checkin_result = pyqtSignal(int)
    control_result = pyqtSignal(bool)
    close_door = pyqtSignal()

    def __init__(self, user):
        super().__init__()
        self.__user = user
        obs.on("closeDoor" , lambda: self.close_door.emit())

    @pyqtSlot()
    def requestCheckin(self):
        try:
            self.__thread_checkin = ThreadCheckin(self.__user)
            self.__thread_checkin.request_result.connect(self.__requestResult)
            self.__thread_checkin.start()
        except Exception:
            writeExceptionToFile()

    @pyqtSlot(int)
    def __requestResult(self, result: int):
        try:
            self.checkin_result.emit(result)
        except Exception:
            writeExceptionToFile()

    @pyqtSlot()
    def requestDropKey(self):
        try:
            self.__thread_control_door = ThreadControlDoor('dropKey')
            self.__thread_control_door.control_result.connect(self.__controlResult)
            self.__thread_control_door.start()
        except Exception:
            writeExceptionToFile()

    @pyqtSlot(bool)
    def __controlResult(self, result: bool):
        try:
            self.control_result.emit(result)
        except Exception:
            writeExceptionToFile()
    
    def closeControlDoor(self):
        obs.off("closeDoor")
        self.__thread_control_door.closeControlDoor()
'''


        
