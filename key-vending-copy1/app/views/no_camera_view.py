from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QSizePolicy
from PyQt5.QtCore import Qt, QMetaObject, QTimer, QRect,QObject
from constant.path import Path
from constant.default_string import DefaultString
from utils.write_log import writeExecutionSteps, writeExceptionToFile
from views.custom_style.label import RedBackgroundBottom, ScreenTitle, Text, GifImage, RedBackgroundTop,LogoApp1
import cv2
from views.scan_qr_view import ScanQRView
import serial
class NoCameraView():
    """ Scan QR Code view
    """
    
    TAG = 'ScanQRView'
    def __init__(self,user,controller,main):
        self.__controller = controller
        self.__main = main
        self.__user = user
        
        #self.ser = serial.Serial('/dev/video0')
        
        writeExecutionSteps(self.TAG)

        self.central_widget = QWidget(main)
        self.central_widget.setFixedSize(self.__main.width, self.__main.height)

        red_background_top = RedBackgroundTop(Path.PATH_ICON + '/logo.png', self.central_widget)
        
        self.logo_no_camera = LogoApp1(Path.PATH_ICON + '/no_camera.png', self.central_widget)
        

        self.screen_title = Text(self.central_widget)
        self.screen_title.setXY(0, int(self.__main.height * 0.55))

        red_background_bottom = RedBackgroundBottom(self.central_widget)

        self.__timer = QTimer()
        self.__timer.timeout.connect(self.backToWelcome)
        self.__timer.start(6000)
        
        #Set timeout after 1s check camera available or not
        self.__timer2 = QTimer()
        self.__timer2.timeout.connect(self.check_cam)
        self.__timer2.start(1000)
        
        
        self.retranslateUI()
        QMetaObject.connectSlotsByName(self.central_widget)
        main.setCentralWidget(self.central_widget)

    def retranslateUI(self):
        default_string = DefaultString.getDefaultString()
        self.screen_title.setText(default_string.NO_CAMERA +'\n'+ default_string.TRY_AGAIN)
        self.screen_title.setTextSize(40)
        
    
    def stopComponentsRunning(self):
        pass

    def backToWelcome(self):
        try:
            self.stopComponentsRunning()
        except Exception:
            writeExceptionToFile()
        finally:
            self.__main.onTransferScreen(screen="startScreenWelcome")

    def check_cam(self):
        video_capture = cv2.VideoCapture(0)
        if video_capture.isOpened():
           video_capture.release()
           self.__main.onTransferScreen("startScreenScanQR")
           
           
                  
          