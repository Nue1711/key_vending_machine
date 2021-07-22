from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QSizePolicy
from PyQt5.QtCore import Qt, QMetaObject, QTimer, QRect, pyqtSlot
from constant.path import Path
from constant.default_string import DefaultString
from utils.write_log import writeExecutionSteps, writeExceptionToFile
from views.custom_style.label import (RedBackgroundBottom, RedBackgroundTop, ScreenTitle, 
                                        NormalText, ConnectionErrorText)
from constant.request_api_result import RequestAPIResult


class WaitQRCodeView():
    """ wait QR code view
    """
    
    TAG = 'WaitQRCodeView'
   

    def __init__(self, user, controller, main):
        self.__controller = controller
        self.__main = main
        self.__user = user

        writeExecutionSteps(self.TAG)

        self.central_widget = QWidget(main)
        self.central_widget.setFixedSize(self.__main.width, self.__main.height)

        red_background_top = RedBackgroundTop(Path.PATH_ICON + '/logo.png', self.central_widget)

        self.screen_title = ScreenTitle(self.central_widget)
        self.screen_title.setXY(0, int(self.__main.height * 0.15))

        self.looking_for_code = NormalText(self.central_widget)
        self.looking_for_code.setXY(0, int(self.__main.height * 0.7))
        
        self.connection_error = ConnectionErrorText(self.central_widget)
        self.connection_error.setHidden(True)

        red_background_bottom = RedBackgroundBottom(self.central_widget)

        self.retranslateUI()
        QMetaObject.connectSlotsByName(self.central_widget)
        main.setCentralWidget(self.central_widget)

        self.__timer = QTimer()
        self.__timer.timeout.connect(self.getInfoResult)
        self.__timer.setSingleShot(True)
        self.__timer.start(6000)
        

    def retranslateUI(self):
        default_string = DefaultString.getDefaultString()

        self.screen_title.setText(default_string.PLEASE_WAIT)
        self.looking_for_code.setText(default_string.LOOKING_FOR_CODE)
        self.connection_error.setText(default_string.NOT_CONNECT_INTERNET)

    def connectionError(self):
        self.connection_error.setHidden(False)

    def stopComponentsRunning(self):
        pass

    def backToWelcome(self):
        try:
            self.stopComponentsRunning()
        except Exception:
            writeExceptionToFile()
        finally:
            self.__main.onTransferScreen(screen="startScreenWelcome")
    
    def getInfoResult(self):
        print(self.__user.qr_code)
        '''
        try:
            self.stopComponentsRunning()
            if result == RequestAPIResult.SUCCESS:
                if 'completed' in self.__user.status:
                    self.__main.onTransferScreen(screen="startScreenQRCodeSuccessPayment")
                else:
                    self.__main.onTransferScreen(screen="startScreenQRCodeSuccess")
            elif result == RequestAPIResult.QR_CODE_NOT_FOUND:
                self.__main.onTransferScreen(screen="startScreenQRCodeNotFound")
            elif result == RequestAPIResult.CONNECTION_ERROR:
                self.connectionError()
                QTimer.singleShot(5000, self.backToWelcome)
            else:
                self.__main.onTransferScreen(screen="startScreenWelcome")
        except Exception:
            writeExceptionToFile()
        ''' 
        try:
            self.stopComponentsRunning()
            if self.__user.qr_code == True:
                   self.__main.onTransferScreen(screen= 'startScreenScanQRTrue') 
            else:
                self.__main.onTransferScreen(screen="startScreenScanQRNotTrue")
        except Exception:
            writeExceptionToFile()   
        
      
         
        
    
    
    
