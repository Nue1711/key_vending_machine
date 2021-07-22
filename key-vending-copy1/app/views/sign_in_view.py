from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QSizePolicy, QLineEdit
from PyQt5.QtCore import Qt, QMetaObject, QTimer, QRect,QObject
from constant.path import Path
from constant.default_string import DefaultString
from utils.write_log import writeExecutionSteps, writeExceptionToFile
from views.custom_style.textbox import TextBox
from views.custom_style.label import RedBackgroundBottom, LogoApp, ScreenTitle, RedBackgroundTop
from views.custom_style.button import NextButton
from views.custom_style.language_combobox import LanguageComboBox
from constant.language import Language
import os
from firebase import firebase
from getpass import getpass
import pyrebase

class SignInView():
    """ SignIn view
    """
    
    TAG = 'SignInView'

    def __init__(self, user, controller, main):
        self.__controller = controller
        self.__main = main
        self.__user = user

        #self.authentication()

        writeExecutionSteps(self.TAG)

        self.central_widget = QWidget(main)
        self.central_widget.setFixedSize(self.__main.width, self.__main.height)

        red_background_top = RedBackgroundTop(Path.PATH_ICON + '/logo.png', self.central_widget)

        self.screen_title = ScreenTitle(self.central_widget)
        self.screen_title.setXY(0, int(self.__main.height * 0.15))
        self.screen_title.setHeight(int(self.__main.height * 0.15))
        self.screen_title.setTextSize(60)

        self.email_label = QLabel(self.central_widget)
        self.email_label.setText("Email")
        self.email_label.setGeometry(330,320,90,60)

        self.password_label = QLabel(self.central_widget)
        self.password_label.setText("Password")
        self.password_label.setGeometry(330,500,90,60)

        self.error_label = QLabel(self.central_widget)
        self.error_label.setStyleSheet("color: red")
        self.error_label.setGeometry(450, 620, 360, 30)
        self.error_label.setVisible(False)

        self.__language_combobox = LanguageComboBox(self.central_widget)
        self.__language_combobox.on_language_changed.connect(self.onLanguageChanged)

        self.text_email_box = TextBox(self.central_widget)
        self.text_email_box.setXY(450, 320, 360, 60)

        self.text_password_box = TextBox(self.central_widget)
        self.text_password_box.setXY(450, 500, 360, 60)
        self.text_password_box.setEchoMode(QLineEdit.Password)

        self.__next_button = NextButton(Path.PATH_ICON + '/next.png',self.central_widget)
        self.__next_button.setSize(int(self.__main.width * 0.20))
        self.__next_button.clicked.connect(self.nextScreenPressed)

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
        self.__next_button.setText(default_string.NEXT)
        self.text_email_box.setPlaceholderText('Please enter your email! ')
        self.text_password_box.setPlaceholderText('Please enter your password!')
            
    def stopComponentsRunning(self):
        pass

    def nextScreenPressed(self):
        self.stopComponentsRunning()
        if str(self.text_email_box.text()) == 'manager171199@gmail.com':
            if str(self.text_password_box.text()) == 'deadpool123':
                self.__main.onTransferScreen("startScreenAdmin") 
            else:
                self.error_label.setText('Incorrect email or password')
                self.error_label.setVisible(True)
        else:
            self.authentication(self.text_email_box.text(), self.text_password_box.text())
         
    def authentication(self, email, password):
        firebaseConfig = {
            "apiKey": "AIzaSyC8y0RxCWL39n7LAToSEJMO8LyuK6fdCps",
            "authDomain": "test-60f7d.firebaseapp.com",
            "databaseURL": "https://test-60f7d-default-rtdb.firebaseio.com",
            "projectId": "test-60f7d",
            "storageBucket": "test-60f7d.appspot.com",
            "messagingSenderId": "564066761719",
            "appId": "1:564066761719:web:22c2072d71db4a1a7e4cf2"
        }
        init_firebase = pyrebase.initialize_app(firebaseConfig)

        auth = init_firebase.auth()
        try:
            login = auth.sign_in_with_email_and_password(email, password)
            id_token = auth.get_account_info(login['idToken'])
            self.__user.user_id = id_token['users'][0]['localId']
            self.__main.onTransferScreen("startScreenScanQR")     
            #self.__main.onTransferScreen("startScreenScanQRTrue")  
        except:
            self.error_label.setText("Incorrect email or password")
            self.error_label.setVisible(True) 
               
    
    def backToWelcome(self):
        try:
            self.stopComponentsRunning()
        except Exception:
            writeExceptionToFile()
        finally:
            self.__main.onTransferScreen(screen="startScreenWelcome")
    
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
