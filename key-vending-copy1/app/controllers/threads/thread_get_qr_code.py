from controllers.parse_json import ParseJson
import time
from PyQt5.QtCore import QThread, pyqtSignal
from utils.validate import checkNull
from constant.request_api_result import RequestAPIResult


class ThreadGetQRCode(QThread):
    request_result = pyqtSignal(int)
    def __init__(self,command, user):
        QThread.__init__(self)
        self.__command = command
        self.__user = user
    def run(self):
        if (self.__command == 'getBooking'):

            self.getBooking()
    
    def getBooking(self):
        parsejson = ParseJson()
        respone = parsejson.parse_json(self.__user.qr_code)
        flag = False
        if respone ==None:
            self.request_result.emit(RequestAPIResult.FAIL)
            return
        elif respone == 'ConnectionError':
            self.request_result.emit(RequestAPIResult.CONNECTION_ERROR)
            return
        elif 'error' in respone:
            if respone['error']['message'] == 'Not found':
                self.request_result.emit(RequestAPIResult.QR_CODE_NOT_FOUND)
            else:
                self.request_result.emit(RequestAPIResult.FAIL)
            return

        status = str(respone['status'].lower())
        if 'checkedin' in status or 'done' in status:
            self.request_result.emit(RequestAPIResult.QR_CODE_NOT_FOUND)
        if 'booking' or 'completed' in status:
            self.__user.name = checkNull(respone['customerName'])
            self.__user.index = checkNull(respone['index'])
            self.__user.status = checkNull(respone['status'])
            self.__user.booking_date = checkNull(respone['bookingDate'])
            self.__user.id = checkNull(respone['id'])
            self.__user.vehicle = checkNull(respone['machineName'])
            print(self.__user.name)
          
        self.request_result.emit(RequestAPIResult.SUCCESS)
        


        


