from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QSizePolicy
from PyQt5.QtCore import Qt, QMetaObject, QTimer, QRect, pyqtSlot
from constant.path import Path
from constant.default_string import DefaultString
from utils.write_log import writeExecutionSteps, writeExceptionToFile
from views.custom_style.label import (RedBackgroundBottom, RedBackgroundTop, ScreenTitle, 
                                        NormalText, ConnectionErrorText)
from constant.request_api_result import RequestAPIResult
import pickle
import face_recognition
import os
class WaitTrainingView():
    """ wait Training view
    """
    
    TAG = 'WaitTrainingView'
   

    def __init__(self, user, controller, main):
        self.__controller = controller
        self.__main = main
        self.__user = user
        self.known_face_names = []

        writeExecutionSteps(self.TAG)

        for users in os.listdir(Path.PATH_IMAGE):
      	    self.known_face_names.append(users)

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
        self.__timer.start(1000)
        

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
        self.all_face_encodings = {}
        for name in self.known_face_names:
       
          for img_path in os.listdir('/home/trung1711/Pictures/key-vending-copy1/app/resources/dataset/{}'.format(name)):
                try:  
                    print(img_path)
                    people_image = face_recognition.load_image_file('/home/trung1711/Pictures/key-vending-copy1/app/resources/dataset/{}/{}'.format(name,img_path))
                    self.all_face_encodings['{}'.format(name)] =  face_recognition.face_encodings(people_image)[0]
                except IndexError:
                    self.__main.onTransferScreen(screen="startScreenWelcome")   
        with open('/home/trung1711/Pictures/key-vending-copy1/app/resources/dataset_faces.dat', 'wb') as f:
            pickle.dump(self.all_face_encodings, f) 
            
        #self.__main.onTransferScreen(screen="startScreenThankYou")
        self.__main.onTransferScreen(screen="startScreenDropKey")
    
  
        
      
         
        
    
    
    
