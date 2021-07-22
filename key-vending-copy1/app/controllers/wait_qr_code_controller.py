from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal,Qt
from utils.write_log import writeExceptionToFile
from controllers.parse_json import ParseJson
from controllers.threads.thread_get_qr_code import ThreadGetQRCode

class WaitQRCodeController(QObject):

    get_info_result = pyqtSignal(int)

    def __init__(self, user):
        super().__init__()
    
        self.__user = user
    
        
     
   
            

    



