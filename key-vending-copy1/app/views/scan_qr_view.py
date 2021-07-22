import cv2
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QSizePolicy, QApplication, QPushButton
from PyQt5.QtCore import Qt, QMetaObject, QTimer, QRect, pyqtSignal,pyqtSlot, QRect,QBasicTimer,QObject
from PyQt5.QtGui import *
from constant.path import Path
from constant.default_string import DefaultString
from utils.write_log import writeExecutionSteps, writeExceptionToFile
from views.custom_style.label import RedBackgroundBottom, ScreenTitle, NormalText, GifImage, RedBackgroundTop,LogoApp1,Text
from views.custom_style.preview_webcam import PreviewWebcamWidget
import face_recognition
import time
from views.face_rec import FaceRec
from views.custom_style.loading import Loading
# from resizeimage import resizeimage

class ScanQRView(QObject):
    """ Scan QR Code view
    """
    
    TAG = 'ScanQRView'

    def __init__(self, user, controller, main):
        super().__init__()  
        self.__controller = controller
        self.__main = main
        self.__user = user
        self.frame =''
        self.count = 0
        
        self.face = FaceRec(self.__user,self.__main)

        self.video_capture = cv2.VideoCapture(0)
        writeExecutionSteps(self.TAG)
      

        self.central_widget = QWidget(main)
        self.central_widget.setFixedSize(self.__main.width, self.__main.height)
        
        self.logo_no_camera = LogoApp1(Path.PATH_ICON + '/no_camera.png', self.central_widget)
        self.logo_no_camera.setHidden(True)


        red_background_top = RedBackgroundTop(Path.PATH_ICON + '/logo.png', self.central_widget)

        self.screen_title = ScreenTitle(self.central_widget)
        self.screen_title.setXY(0, int(self.__main.height * 0.15))
        self.screen_title.setHeight(int(self.__main.height * 0.15))
        self.screen_title.setTextSize(60)
        

        self.screen_normal = NormalText(self.central_widget)
        self.screen_normal.setXY(0, int(self.__main.height * 0.15))
        self.screen_normal.setHeight(int(self.__main.height * 0.25))
        self.screen_normal.setTextSize(40)

        self.screen_title1 = Text(self.central_widget)
        self.screen_title1.setXY(0, int(self.__main.height * 0.55))
        self.screen_title1.setTextSize(40)
        self.screen_title1.setVisible(False)
       

        self.__preview = PreviewWebcamWidget(self.central_widget)
        self.__preview.setGeometry(QRect(280,300,220,200))
       
        red_background_bottom = RedBackgroundBottom(self.central_widget)

        #use QBasicTimer create a thread run camera on widget
        self.__timer = QBasicTimer()
        self.__timer.start(0,self)

        self.__timer2 = QTimer()
        self.__timer2.timeout.connect(self.p)
        self.__timer2.start(5000)

        self.__timer3 = QTimer()
        self.__timer3.timeout.connect(self.backToWelcome)
        self.__timer3.start(70000)

        self.loading = Loading(self.central_widget)

        self.retranslateUI()
        QMetaObject.connectSlotsByName(self.central_widget)
        main.setCentralWidget(self.central_widget)

    def retranslateUI(self):
        default_string = DefaultString.getDefaultString()

        self.screen_title.setText(default_string.PLEASE_SHOW_QR)
        self.screen_normal.setText(default_string.PLEASE_SHOW_QR_INFO)
        self.screen_title1.setText(default_string.NO_CAMERA +'\n'+ default_string.TRY_AGAIN)
    
    def stopComponentsRunning(self):
        self.__timer.stop()

    def backToWelcome(self):
        try:
            self.stopComponentsRunning()
        except Exception:
            writeExceptionToFile()
        finally:
            self.__main.onTransferScreen(screen="startScreenWelcome")
        
    def timerEvent(self, event):
        
           ret, self.frame = self.video_capture.read()
           self.__preview.imageDataSlot(self.frame)
        
    
    #compare frame with image is match or not
    def p(self):  
        self.face.face_rec(self.frame)
        self.loading.startLoading()# run spiner
        self.count+=1
        if self.count == 3:
           try: 
             self.stopComponentsRunning()
           finally:  
             self.__main.onTransferScreen(screen="startScreenWaitQRCode")
      

   
    
    

        
      
        


        
        

   


    
       
        

        
        
        
       
        
       
        
        

        
     
                    
