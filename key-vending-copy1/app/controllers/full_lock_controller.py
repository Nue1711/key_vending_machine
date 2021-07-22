from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from utils.write_log import writeExceptionToFile
#from controllers.threads.thread_checkin import ThreadCheckin
#from controllers.threads.thread_control_door import ThreadControlDoor
#from utils.observable_trigger import ObservableTrigger
#obs = ObservableTrigger.getInstance()

class FullLockController(QObject):
    def __init__(self, user):
        super().__init__()
        self.__user = user
        pass