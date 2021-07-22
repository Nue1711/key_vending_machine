from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from utils.write_log import writeExceptionToFile


class TakeKeyController(QObject):

    def __init__(self, user):
        super().__init__()
        self.__user = user
        pass
        # obs.on("closeDoor" , lambda: self.clo?

    # @pyqtSlot()
    # def requestDone(self):
    #     try:
    #         self.__thread_done = ThreadDone(self.__user)
    #         self.__thread_done.request_result.connect(self.__requestResultDone)
    #         self.__thread_done.start()
    #     except Exception:
    #         writeExceptionToFile()

    # @pyqtSlot(int)
    # def __requestResultDone(self, result: int):
    #     try:
    #         self.done_result.emit(result)
    #     except Exception:
    #         writeExceptionToFile()
    
    # @pyqtSlot()
    # def requestTakeKey(self):
    #     try:
    #         key_number = int(self.__user.key_position)
    #         self.__thread_control_door = ThreadControlDoor('takeKey', key_number)
    #         self.__thread_control_door.control_result.connect(self.__controlResult)
    #         self.__thread_control_door.start()
    #     except Exception:
    #         writeExceptionToFile()

    # @pyqtSlot(bool)
    # def __controlResult(self, result: bool):
    #     try:
    #         self.control_result.emit(result)
    #     except Exception:
    #         writeExceptionToFile()

    # def closeControlDoor(self):
    #     obs.off("closeDoor")
    #     self.__thread_control_door.closeControlDoor()