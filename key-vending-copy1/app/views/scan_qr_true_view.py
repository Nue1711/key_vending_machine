from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QSizePolicy
from PyQt5.QtCore import Qt, QMetaObject, QTimer, QRect
from constant.path import Path
from views.custom_style.button import NextButton
from constant.default_string import DefaultString
from utils.write_log import writeExecutionSteps, writeExceptionToFile
from views.custom_style.label import RedBackgroundBottom, ScreenTitle, Text, GifImage, RedBackgroundTop
from datetime import datetime
from firebase import firebase
class ScanQRTrueView():
    """ Scan QR Code view
    """
    
    TAG = 'ScanQRView'

    def __init__(self, user, controller, main):
        self.__controller = controller
        self.__main = main
        self.__user = user
        
        writeExecutionSteps(self.TAG)

        now = datetime.now()
        self.__user.check_in_date = now.strftime('%H:%M:%S')

        # self.firebase = firebase.FirebaseApplication("https://test-60f7d-default-rtdb.firebaseio.com/", None)
        # self.result = self.firebase.get('Customer1/' + self.__user.name, '')
        # self.__user.phone_number = self.result['phone_number']
        # self.__user.plate_number = self.result['plate_number']


        self.central_widget = QWidget(main)
        self.central_widget.setFixedSize(self.__main.width, self.__main.height)

        red_background_top = RedBackgroundTop(Path.PATH_ICON + '/logo.png', self.central_widget)

        self.screen_title = Text(self.central_widget)
        self.screen_title.setXY(0, int(self.__main.height * 0.15))
        self.screen_title.setHeight(int(self.__main.height * 0.5))
        self.screen_title.setTextSize(40)
        
        self.__next_button = NextButton(Path.PATH_ICON + '/next.png',self.central_widget)
        self.__next_button.setWidth(int(self.__main.width * 0.20))
        self.__next_button.clicked.connect(self.nextScreenPressed)

        red_background_bottom = RedBackgroundBottom(self.central_widget)

        self.__timer = QTimer()
        self.__timer.timeout.connect(self.backToWelcome)
        self.__timer.setSingleShot(True)
        self.__timer.start(60000)


        self.retranslateUI()
        QMetaObject.connectSlotsByName(self.central_widget)
        main.setCentralWidget(self.central_widget)

    def retranslateUI(self):
        default_string = DefaultString.getDefaultString()
        self.screen_title.setText("QR Ok\n" + default_string.HELLO + ' ' +self.__user.name +'\n' + default_string.YOUR_VEHICLE +self.__user.plate_number+'\n'+default_string.YOUR_PHONE_NUMBER + self.__user.phone_number +'\n' +default_string.SUB_CAR +'\n'+default_string.PLEASE_DROP_KEY+ '\n' +self.__user.id)
        
    
    def stopComponentsRunning(self):
        pass

    def backToWelcome(self):
        try:
            self.stopComponentsRunning()
        except Exception:
            writeExceptionToFile()
        finally:
            self.__main.onTransferScreen(screen="startScreenWelcome")
            
    def nextScreenPressed(self):
        self.__main.onTransferScreen(screen="startScreenTakeKey")
