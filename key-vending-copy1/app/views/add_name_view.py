from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QSizePolicy
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

class AddNameView():
    """ Welcome view
    """
    
    TAG = 'WelcomeView'

    def __init__(self, user, controller, main):
        self.__controller = controller
        self.__main = main
        self.__user = user
        #self.cap = cv2.VideoCapture(0)
        self.known_face_names = []
        for users in os.listdir(Path.PATH_IMAGE):
      	    self.known_face_names.append(users)


        writeExecutionSteps(self.TAG)

        self.central_widget = QWidget(main)
        self.central_widget.setFixedSize(self.__main.width, self.__main.height)

        red_background_top = RedBackgroundTop(Path.PATH_ICON + '/logo.png', self.central_widget)

        self.screen_title = ScreenTitle(self.central_widget)
        self.screen_title.setXY(0, int(self.__main.height * 0.15))
        self.screen_title.setHeight(int(self.__main.height * 0.15))
        self.screen_title.setTextSize(60)

        self.error_label = QLabel(self.central_widget)
        self.error_label.setStyleSheet("color: red")
        self.error_label.setGeometry(450, 620, 360, 30)
        self.error_label.setText("Invalid name/phone number, Try again!")
        self.error_label.setVisible(False)

        self.__language_combobox = LanguageComboBox(self.central_widget)
        self.__language_combobox.on_language_changed.connect(self.onLanguageChanged)

        self.text_name_box = TextBox(self.central_widget)
      
        self.text_name_box.setXY(450, 280, 360, 60)
        self.text_phone_number_box = TextBox(self.central_widget)
        self.text_phone_number_box.setXY(450, 410, 360, 60)

        self.text_number_plate_box = TextBox(self.central_widget)
        self.text_number_plate_box.setXY(450, 540, 360, 60)

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
        self.screen_title.setText(default_string.SIGN_UP)
        self.__next_button.setText(default_string.NEXT)
        self.text_name_box.setPlaceholderText('Please text your name! ')
        self.text_phone_number_box.setPlaceholderText('Please text your phone number!')
        self.text_number_plate_box.setPlaceholderText('Please text your number plate!')

       
    def stopComponentsRunning(self):
        pass

    def nextScreenPressed(self):
        self.stopComponentsRunning()
        if  not str(self.text_phone_number_box.text()).isnumeric() or len(str(self.text_phone_number_box.text())) == 0 :
            self.error_label.setVisible(True)

        elif "Please" in  str(self.text_name_box.text()) or  str(self.text_name_box.text()) == '':
            self.error_label.setVisible(True)

        elif str(self.text_name_box.text()) in self.known_face_names:
            self.error_label.setVisible(True)

        elif "Please" in str(self.text_number_plate_box.text()) or str(self.text_number_plate_box.text()) == '':
            self.error_label.setVisible(True)
        else:
            self.__user.name = str(self.text_name_box.text())
            self.__user.phone_number = str(self.text_phone_number_box.text())
            self.__user.plate_number = str(self.text_number_plate_box.text())

            #self.__main.onTransferScreen("startScreenTrainingFace")
            self.__main.onTransferScreen("startScreenSignUp")

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
