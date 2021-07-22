import cv2
import os
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QSizePolicy, QApplication, QPushButton
from PyQt5.QtCore import Qt, QMetaObject, QTimer, QRect, pyqtSignal,pyqtSlot, QRect,QBasicTimer,QObject
from PyQt5.QtGui import *
from constant.path import Path
from constant.default_string import DefaultString
from views.custom_style.button import StartButton
from utils.write_log import writeExecutionSteps, writeExceptionToFile
from views.custom_style.label import RedBackgroundBottom, ScreenTitle, NormalText, GifImage, RedBackgroundTop,LogoApp1,Text
from views.custom_style.preview_webcam import PreviewWebcamWidget
import time
from views.custom_style.loading import Loading
# from resizeimage import resizeimage

class TrainingFaceView(QObject):
    """ Training Face view
    """
    
    TAG = 'TrainingFaceView'

    def __init__(self, user, controller, main):
        super().__init__()  
        self.__controller = controller
        self.__main = main
        self.__user = user
        self.frame = ''
        self.resize_frame = ''
        self.count = 0
        
        
        self.new_path = os.path.join(Path.PATH_PARENT, self.__user.name)
        if not os.path.exists(self.new_path):
            os.mkdir(self.new_path)
            
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

        self.__start_button = StartButton(self.central_widget)
        self.__start_button.clicked.connect(self.nextScreenPressed)
        self.__start_button.setXY(480, 750, 340, 100)
        

        # self.screen_normal = NormalText(self.central_widget)
        # self.screen_normal.setXY(0, int(self.__main.height * 0.15))
        # self.screen_normal.setHeight(int(self.__main.height * 0.25))
        # self.screen_normal.setTextSize(40)

        self.screen_title1 = Text(self.central_widget)
        self.screen_title1.setXY(0, int(self.__main.height * 0.55))
        self.screen_title1.setTextSize(40)
        self.screen_title1.setStartHidden()
       

        self.__preview = PreviewWebcamWidget(self.central_widget)
        self.__preview.setGeometry(QRect(320,300,220,200))
       
        red_background_bottom = RedBackgroundBottom(self.central_widget)

        #use QBasicTimer create a thread run camera on widget
        self.__timer = QBasicTimer()
        self.__timer.start(0,self)

        # self.__timer2 = QTimer()
        # self.__timer2.timeout.connect(self.p)
        # self.__timer2.start(1000)

        self.retranslateUI()
        QMetaObject.connectSlotsByName(self.central_widget)
        main.setCentralWidget(self.central_widget)

    def retranslateUI(self):
        default_string = DefaultString.getDefaultString()

        self.screen_title.setText(default_string.TRAINING_FACE)
        self.__start_button.setText(default_string.TAKE_PIC)
        #self.screen_normal.setText(default_string.WAIT)
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
    
    # def p(self): 
    #     if self.count == 1:
    #         self.__main.onTransferScreen(screen="startScreenWaitTraining")

    #     elif  self.count<1:
    #         self.resize_frame = cv2.resize(src = self.frame, dsize = (170,128), interpolation = cv2.INTER_AREA)
    #         cv2.imwrite('/home/trung1711/Videos/key-vending-copy1/app/resources/dataset/{}/{}_{}{}'.format(self.__user.name,self.__user.name,str(self.count),'.jpg'), self.resize_frame)
    #         print(self.count)
            # self.count += 1
    def nextScreenPressed(self):
        
        if self.count < 5:
            self.resize_frame = cv2.resize(src = self.frame, dsize = (170,128), interpolation = cv2.INTER_AREA)
            cv2.imwrite('/home/trung1711/Pictures/key-vending-copy1/app/resources/dataset/{}/{}_{}{}'.format(self.__user.name,self.__user.name,str(self.count),'.jpg'), self.resize_frame)
            self.count +=1
        elif self.count == 5:
            self.__main.onTransferScreen(screen="startScreenWaitTraining")

       

            


            
            
           
           
        


   
    
    

        
      
        


        
        

   


    
       
        

        
        
        
       
        
       
        
        

        
     
                    
