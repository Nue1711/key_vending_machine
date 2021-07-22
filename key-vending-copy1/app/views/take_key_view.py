from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QSizePolicy
from PyQt5.QtCore import Qt, QMetaObject, QTimer, QRect
from constant.path import Path
from constant.default_string import DefaultString
from utils.write_log import writeExecutionSteps, writeExceptionToFile
from views.custom_style.label import RedBackgroundBottom, RedBackgroundTop, ScreenTitle, NormalText, ConnectionErrorText
from constant.request_api_result import RequestAPIResult
import time
from firebase import firebase

class TakeKeyView():
    """ Take key to the locker view
    """
    
    TAG = 'TakeKeyView'

    def __init__(self, user, controller, main):
        self.__controller = controller
        self.__main = main
        self.__user = user

        writeExecutionSteps(self.TAG)

        self.central_widget = QWidget(main)
        self.central_widget.setFixedSize(self.__main.width, self.__main.height)

        self.firebase = firebase.FirebaseApplication("https://test-60f7d-default-rtdb.firebaseio.com/", None)
        self.result = self.firebase.put('/Customer/' + self.__user.user_id , 'door_status', 'Open')

        red_background_top = RedBackgroundTop(Path.PATH_ICON + '/logo.png', self.central_widget)

        self.screen_title = ScreenTitle(self.central_widget)
        self.screen_title.setXY(0, int(self.__main.height * 0.15))
        self.screen_title.setHeight(int(self.__main.height * 0.3))
        self.screen_title.setTextSize(100)

        self.content = NormalText(self.central_widget)
        self.content.setXY(0, int(self.__main.height * 0.7))

        self.connection_error = ConnectionErrorText(self.central_widget)

        red_background_bottom = RedBackgroundBottom(self.central_widget)

        self.retranslateUI()
        QMetaObject.connectSlotsByName(self.central_widget)
        main.setCentralWidget(self.central_widget)
        
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.__closeDoor)
        self.__timer.setSingleShot(True)
        self.__timer.start(2000)

    def retranslateUI(self):
        self.__default_string = DefaultString.getDefaultString()
        self.screen_title.setText(self.__default_string.TAKE_KEY)
        self.content.setText(self.__default_string.DOOR_OPENING)

    def connectionError(self):
        self.connection_error.setText(self.__default_string.NOT_CONNECT_INTERNET)

    def fail(self):
        self.connection_error.setText(self.__default_string.TRY_AGAIN)

    def stopComponentsRunning(self):
        self.__timer.stop()
        self.__controller.closeControlDoor()

    def backToWelcome(self):
        try:
            self.stopComponentsRunning()
        except Exception:
            writeExceptionToFile()
        finally:
            self.__main.onTransferScreen(screen="startScreenWelcome")

    def __closeDoor(self):
        self.__count_timer_close_door = 15
        self.__timer_close_door = QTimer()
        self.__timer_close_door.timeout.connect(self.__updateCloseDoorTimeText)
        self.__timer_close_door.start(1000)

    def __updateCloseDoorTimeText(self):
        self.__count_timer_close_door -= 1

        second = self.__default_string.SECONDS
        if self.__count_timer_close_door == 1:
            second = self.__default_string.SECOND

        if self.__count_timer_close_door == 0:
            self.__timer_close_door.stop()        
            self.content.setText(self.__default_string.SHUT_DOOR)
            
            self.__main.onTransferScreen(screen="startScreenThankAnother")
            
        else:
            self.content.setText(self.__default_string.DOOR_WILL_CLOSE 
            + ' ' 
            + str(self.__count_timer_close_door)
            + ' '
            + second)
