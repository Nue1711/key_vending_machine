from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QSizePolicy
from PyQt5.QtCore import Qt, QMetaObject, QTimer, QRect
from constant.path import Path
from firebase import firebase
from constant.default_string import DefaultString
from utils.write_log import writeExecutionSteps, writeExceptionToFile
from views.custom_style.label import RedBackgroundBottom, ScreenTitle, Text, GifImage, RedBackgroundTop
from datetime import datetime
from views.data import Data
import random
class ThankYouViewView():
    """ Thank You view
    """
    
    TAG = 'Thank You View'

    def __init__(self, user, controller, main):
        self.__controller = controller
        self.__main = main
        self.__user = user
            
        writeExecutionSteps(self.TAG)
        
        now = datetime.now()
        self.__user.check_out_date = now.strftime('%H:%M:%S')

        dt = datetime.today()
        self.__user.done_date = dt.strftime('%y/%m/%d')
        self.key_lock = random.randint(0,30)
        if self.key_lock in Data.KEY_LOCK_NUMBER:
            self.key_lock = random.randint(0,30)
        
        self.firebase = firebase.FirebaseApplication("https://test-60f7d-default-rtdb.firebaseio.com/", None)
        self.result = self.firebase.put('/Customer/'+ self.__user.user_id , 'name', self.__user.name)
        self.result = self.firebase.put('/Customer/'+ self.__user.user_id , 'phone_number', self.__user.phone_number)
        self.result = self.firebase.put('/Customer/'+ self.__user.user_id , 'plate_number', self.__user.plate_number)
        self.result = self.firebase.put('/Customer/'+ self.__user.user_id , 'date', self.__user.done_date)
        self.result = self.firebase.put('/Customer/'+ self.__user.user_id , 'user_id', self.__user.user_id)
        self.result = self.firebase.put('/Customer/'+ self.__user.user_id , 'check_in_time', self.__user.check_in_date)
        self.result = self.firebase.put('/Customer/'+ self.__user.user_id , 'check_out_time', self.__user.check_out_date)
        self.result = self.firebase.put('/Customer/'+ self.__user.user_id , 'door_status', 'Closed')
        self.result = self.firebase.put('/Customer/'+ self.__user.user_id , 'key_lock_number', str(self.key_lock))
        

        self.central_widget = QWidget(main)
        self.central_widget.setFixedSize(self.__main.width, self.__main.height)

        red_background_top = RedBackgroundTop(Path.PATH_ICON + '/logo.png', self.central_widget)

        self.screen_title = Text(self.central_widget)
        self.screen_title.setXY(0, int(self.__main.height * 0.15))
        self.screen_title.setHeight(int(self.__main.height * 0.5))
        self.screen_title.setTextSize(40)

        self.__timer = QTimer()
        self.__timer.timeout.connect(self.backToWelcome)
        self.__timer.setSingleShot(True)
        self.__timer.start(6000)

        red_background_bottom = RedBackgroundBottom(self.central_widget)
        
        self.retranslateUI()
        QMetaObject.connectSlotsByName(self.central_widget)
        main.setCentralWidget(self.central_widget)

    def retranslateUI(self):
        default_string = DefaultString.getDefaultString()
        self.screen_title.setText(default_string.THANK_YOU + ' and' +default_string.HAVE_A_NICE_DAY)
        
    
    def stopComponentsRunning(self):
        pass

    def backToWelcome(self):
        try:
            self.stopComponentsRunning()
        except Exception:
            writeExceptionToFile()
        finally:
            self.__main.onTransferScreen(screen="startScreenWelcome")
