from PyQt5.QtCore import QObject, pyqtSlot
from utils.write_log import writeExceptionToFile
from controllers.threads.thread_control_door import ThreadControlDoor

class WelcomeController(QObject):
    def __init__(self, user):
        super().__init__()
        self.__is_stop_check_door = False
        self.__is_close_take_key_door = False
        self.__is_close_return_key_door = False

    def checkAndCloseDoor(self):
        while not self.__is_stop_check_door:
            try:
                # take key door opening
                if checkEnableBitDoor(self.__control.getDoorStatus(False),11):  
                    self.__is_close_take_key_door = self.__control.toggleTakeDoor(is_open_door=False) 
                # take key door closing
                else:
                    self.__is_close_take_key_door = True

                # return key door opening
                if checkEnableBitDoor(self.__control.getDoorStatus(True),11):
                    self.__is_close_return_key_door = self.__control.toggleReturnDoor(is_open_door=False)
                # return key door closing
                else:
                    self.__is_close_return_key_door = True
            except Exception:
                writeExceptionToFile()
                continue
            
            if self.__is_close_take_key_door and self.__is_close_return_key_door:
                return True

    def stopCheckDoor(self):
        self.__is_stop_check_door = True
        self.__control.close()
