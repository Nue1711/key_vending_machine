from PyQt5.QtCore import QObject, pyqtSlot
from utils.write_log import writeExceptionToFile
from controllers.threads.thread_control_door import ThreadControlDoor

class AddNameController(QObject):
    def __init__(self, user):
        super().__init__()
        pass

