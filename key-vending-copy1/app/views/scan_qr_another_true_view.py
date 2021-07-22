from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QSizePolicy
from PyQt5.QtCore import Qt, QMetaObject, QTimer, QRect
from constant.path import Path
from constant.default_string import DefaultString
from utils.write_log import writeExecutionSteps, writeExceptionToFile
from views.custom_style.label import RedBackgroundBottom, ScreenTitle, Text, GifImage, RedBackgroundTop

class ScanQRAnotherTrueView():
    """ Scan QR Code view
    """
    
    TAG = 'ScanQRView'

    def __init__(self, user, controller, main):
        self.__controller = controller
        self.__main = main
        self.__user = user
        
        writeExecutionSteps(self.TAG)

        self.central_widget = QWidget(main)
        self.central_widget.setFixedSize(self.__main.width, self.__main.height)

        red_background_top = RedBackgroundTop(Path.PATH_ICON + '/logo.png', self.central_widget)

        self.screen_title = Text(self.central_widget)
        self.screen_title.setXY(0, int(self.__main.height * 0.15))
        self.screen_title.setHeight(int(self.__main.height * 0.5))
        self.screen_title.setTextSize(40)

        

        

        red_background_bottom = RedBackgroundBottom(self.central_widget)
        
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.to_drop_sub_key)
        self.__timer.setSingleShot(True)
        self.__timer.start(6000)
        
        self.retranslateUI()
        QMetaObject.connectSlotsByName(self.central_widget)
        main.setCentralWidget(self.central_widget)

    def retranslateUI(self):
        default_string = DefaultString.getDefaultString()
        self.screen_title.setText("QR Ok\n" + default_string.HELLO + self.__user.name+'\n' + default_string.YOUR_VEHICLE +self.__user.vehicle+'-101 is ready\n'+default_string.OPEN_BALANCE + str(self.__user.balance) )
        
    
    def stopComponentsRunning(self):
        pass

    def backToWelcome(self):
        try:
            self.stopComponentsRunning()
        except Exception:
            writeExceptionToFile()
        finally:
            self.__main.onTransferScreen(screen="startScreenWelcome")
            
    def to_drop_sub_key(self):

        self.__main.onTransferScreen(screen="startScreenDropSubKey")