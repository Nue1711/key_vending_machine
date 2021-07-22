from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QSizePolicy
from PyQt5.QtCore import Qt, QMetaObject, QTimer, QRect,QObject
from constant.path import Path
from constant.default_string import DefaultString
from utils.write_log import writeExecutionSteps, writeExceptionToFile
from views.custom_style.label import RedBackgroundBottom, LogoApp, ScreenTitle
from views.custom_style.button import StartButton
from views.custom_style.language_combobox import LanguageComboBox
from constant.language import Language
from views.data import Data
class LoginView():
    """ Welcome view
    """
    
    TAG = 'WelcomeView'

    def __init__(self, user, controller, main):
        self.__controller = controller
        self.__main = main
        #self.cap = cv2.VideoCapture(0)


        writeExecutionSteps(self.TAG)

        self.central_widget = QWidget(main)
        self.central_widget.setFixedSize(self.__main.width, self.__main.height)

        self.screen_title = ScreenTitle(self.central_widget)
        self.screen_title.setXY(0, int(self.__main.height * 0.08))

        self.__sign_up_button = StartButton(self.central_widget)
        self.__sign_up_button.clicked.connect(self.signUpPressed)
        self.__sign_up_button.setXY(520, 290, 300, 100)

        self.__start_button = StartButton(self.central_widget)
        self.__start_button.clicked.connect(self.nextScreenPressed)
        self.__start_button.setXY(520, 610, 320, 100)

        self.__timer = QTimer()
        self.__timer.timeout.connect(self.backToWelcome)
        self.__timer.setSingleShot(True)
        self.__timer.start(60000)

        red_background_bottom = RedBackgroundBottom(self.central_widget)

        self.retranslateUI()
        QMetaObject.connectSlotsByName(self.central_widget)
        main.setCentralWidget(self.central_widget)

    def retranslateUI(self):
        default_string = DefaultString.getDefaultString()

        self.screen_title.setText(default_string.LOGIN)
        self.__sign_up_button.setText(default_string.SIGNUP)
        self.__start_button.setText(default_string.SIGN_IN)

    def stopComponentsRunning(self):
        pass

    def nextScreenPressed(self):
        self.stopComponentsRunning()
        self.__main.onTransferScreen("startScreenSignIn")

    def signUpPressed(self):
        self.stopComponentsRunning()
        if len(Data.KEY_LOCK_NUMBER) == 30:
           self.__main.onTransferScreen("startScreenFullLock") 
        else:
           self.__main.onTransferScreen("startScreenAddName")
    
    def backToWelcome(self):
        try:
            self.stopComponentsRunning()
        except Exception:
            writeExceptionToFile()
        finally:
            self.__main.onTransferScreen(screen="startScreenWelcome")
           

    