from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QSizePolicy
from PyQt5.QtCore import Qt, QMetaObject, QTimer, QRect,QObject
from constant.path import Path
from constant.default_string import DefaultString
from utils.write_log import writeExecutionSteps, writeExceptionToFile
from views.custom_style.label import RedBackgroundBottom, LogoApp, ScreenTitle
from views.custom_style.button import StartButton
from views.custom_style.language_combobox import LanguageComboBox
from constant.language import Language

class WelcomeView():
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

        logo_app = LogoApp(Path.PATH_ICON + '/logo.png', self.central_widget)

        self.screen_title = ScreenTitle(self.central_widget)
        self.screen_title.setXY(0, int(self.__main.height * 0.25))

        self.__language_combobox = LanguageComboBox(self.central_widget)
        self.__language_combobox.on_language_changed.connect(self.onLanguageChanged)
        #self.__language_combobox.setCurrentIndex(self.getCurrentIndexLanguage())

        self.__start_button = StartButton(self.central_widget)
        self.__start_button.clicked.connect(self.nextScreenPressed)

        red_background_bottom = RedBackgroundBottom(self.central_widget)

        self.retranslateUI()
        QMetaObject.connectSlotsByName(self.central_widget)
        main.setCentralWidget(self.central_widget)

    def retranslateUI(self):
        default_string = DefaultString.getDefaultString()

        self.screen_title.setText(default_string.WELCOME)
        self.__start_button.setText(default_string.START)

    def stopComponentsRunning(self):
        pass

    def nextScreenPressed(self):
        self.stopComponentsRunning()

        # if not self.cap.isOpened():
        #  self.__main.onTransferScreen("startScreenThankYou")
        #  self.cap.release()
        #else:
        self.__main.onTransferScreen("startScreenLogin")
        #self.__main.onTransferScreen('startScreenScanQR')  
        #self.__main.onTransferScreen('startScreenWaitTraining') 

    def onLanguageChanged(self, language):
        if language == "FI":
            Language.setLanguage(Language.FI)
        else:   
            Language.setLanguage(Language.EN)
        
        self.retranslateUI()

    def getCurrentIndexLanguage(self):
        language = Language.getLanguage()
        if language == Language.FI:
            return 0
        else:   
            return 1