from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QSizePolicy, QListWidget, QPushButton
from PyQt5.QtCore import Qt, QMetaObject, QTimer, QRect,QObject, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont
from constant.path import Path
from constant.default_string import DefaultString
from utils.write_log import writeExecutionSteps, writeExceptionToFile
from views.custom_style.label import RedBackgroundBottom, LogoApp, ScreenTitle, RedBackgroundTop
from views.custom_style.button import StartButton
from views.custom_style.language_combobox import LanguageComboBox
from constant.language import Language
from firebase import firebase
from views.data import  Data
class AdminView():
    """ Admin view
    """
    
    TAG = 'AdminView'

    def __init__(self, user, controller, main):
        self.__controller = controller
        self.__main = main
       
        writeExecutionSteps(self.TAG)

        self.arr = []
        print(Data.KEY_LOCK_NUMBER)
        self.firebase = firebase.FirebaseApplication("https://test-60f7d-default-rtdb.firebaseio.com/", None)
        self.result = self.firebase.get('Customer/', '')

        self.central_widget = QWidget(main)
        self.central_widget.setFixedSize(self.__main.width, self.__main.height)

        self.list_label = QLabel(self.central_widget)
        self.list_label.setGeometry(140, 230, 500, 30)
        self.list_label.setText('Customer List')
        self.list_label.setFont(QFont('Time', 20))

        self.list_view = QListWidget(self.central_widget)
        self.list_view.setSpacing(5)
        self.list_view.setGeometry(140, 300, 500, 580)
        self.list_view.clicked.connect(self.listview_clicked)

        self.login_label = QLabel(self.central_widget)
        self.login_label.setScaledContents(True)
        self.login_label.setPixmap(QPixmap(Path.PATH_ICON + '/1.png'))
        self.login_label.setGeometry(500, 0, 290, 180)

        self.welcome_label = QLabel(self.central_widget)
        self.welcome_label.setText("Welcome Admin")
        self.welcome_label.setFont(QFont('Time', 30))
        self.welcome_label.setGeometry(500, 160, 340, 80)


        self.back_button = QPushButton(self.central_widget)
        self.back_button.setGeometry(140, 30, 150, 90)
        self.back_button.clicked.connect(self.backToSignIn)
        self.back_button.setIcon(QIcon(Path.PATH_ICON + '/left.png'))
        self.back_button.setStyleSheet('background-color: rgb(255, 255, 255); border: 5px solid rgb(227, 0, 43)')

        self.back_button.setIconSize(QSize(100,100))

        self.reload_button = QPushButton(self.central_widget)
        self.reload_button.setGeometry(1000, 30, 150, 90)
        self.reload_button.clicked.connect(self.reloadData)
        self.reload_button.setStyleSheet('background-color: rgb(255, 255, 255); border: 5px solid rgb(227, 0, 43)')
        self.reload_button.setIcon(QIcon(Path.PATH_ICON + '/reload.png'))
        self.reload_button.setIconSize(QSize(80,80))

        for item in self.result:
            
            self.list_view.addItem(self.result[item]['name'])
            self.arr.append(item)
        
        self.name_label = QLabel(self.central_widget)
        self.name_label.setGeometry(800, 300, 150, 40)
        self.name_label.setText("<font color = 'white'> ID </font>")
        self.name_label.setStyleSheet('background-color: rgb(227, 0, 43); border-radius: 10px')
        self.name_label.setAlignment(Qt.AlignCenter)

        self.customer_label = QLabel(self.central_widget)
        self.customer_label.setGeometry(1000, 300, 150, 40)
        self.customer_label.setText("<font color = 'white'>Key Lock Number</font>")
        self.customer_label.setStyleSheet('background-color: rgb(227, 0, 43); border-radius: 10px')
        self.customer_label.setAlignment(Qt.AlignCenter)
        
        self.name_label_1 = QLabel(self.central_widget)
        self.name_label_1 .setGeometry(770, 375, 250, 40)
        self.name_label_1 .setStyleSheet('background-color: white; border-radius: 10px')
        #self.name_label_1 .setAlignment(Qt.AlignCenter)


        self.customer_label_1 = QLabel(self.central_widget)
        self.customer_label_1.setGeometry(1000, 375, 150, 40)
        self.customer_label_1.setStyleSheet('background-color:white; border-radius: 10px')
        self.customer_label_1.setAlignment(Qt.AlignCenter)

        self.date_label = QLabel(self.central_widget)
        self.date_label.setGeometry(800, 450, 150, 40)
        self.date_label.setText("<font color = 'white'> Date </font>")
        self.date_label.setStyleSheet('background-color: rgb(227, 0, 43); border-radius: 10px')
        self.date_label.setAlignment(Qt.AlignCenter)

        self.door_label = QLabel(self.central_widget)
        self.door_label.setGeometry(1000, 450, 150, 40)
        self.door_label.setText("<font color = 'white'>Door Status</font>")
        self.door_label.setStyleSheet('background-color: rgb(227, 0, 43); border-radius: 10px')
        self.door_label.setAlignment(Qt.AlignCenter)

        self.date_label_1 = QLabel(self.central_widget)
        self.date_label_1.setGeometry(800, 525, 150, 40)
        self.date_label_1.setStyleSheet('background-color: white; border-radius: 10px')
        self.date_label_1.setAlignment(Qt.AlignCenter)

        self.door_label_1 = QLabel(self.central_widget)
        self.door_label_1 .setGeometry(1000, 525, 150, 40)
        self.door_label_1 .setStyleSheet('background-color: white; border-radius: 10px')
        self.door_label_1 .setAlignment(Qt.AlignCenter)
        
        self.check_in_label = QLabel(self.central_widget)
        self.check_in_label.setGeometry(800, 600, 150, 40)
        self.check_in_label.setText("<font color = 'white'> Check in time </font>")
        self.check_in_label.setStyleSheet('background-color: rgb(227, 0, 43); border-radius: 10px')
        self.check_in_label.setAlignment(Qt.AlignCenter)

        self.plate_label = QLabel(self.central_widget)
        self.plate_label.setGeometry(1000, 600, 150, 40)
        self.plate_label.setText("<font color = 'white'>Plate number </font>")
        self.plate_label.setStyleSheet('background-color: rgb(227, 0, 43); border-radius: 10px')
        self.plate_label.setAlignment(Qt.AlignCenter)

        self.check_in_label_1 = QLabel(self.central_widget)
        self.check_in_label_1.setGeometry(800, 675, 150, 40)
        self.check_in_label_1.setStyleSheet('background-color: white; border-radius: 10px')
        self.check_in_label_1.setAlignment(Qt.AlignCenter)

        self.plate_label_1 = QLabel(self.central_widget)
        self.plate_label_1.setGeometry(1000, 675, 150, 40)
        self.plate_label_1.setStyleSheet('background-color: white; border-radius: 10px')
        self.plate_label_1.setAlignment(Qt.AlignCenter)

        self.check_out_label = QLabel(self.central_widget)
        self.check_out_label.setGeometry(800, 750, 150, 40)
        self.check_out_label.setText("<font color = 'white'> Check out time </font>")
        self.check_out_label.setStyleSheet('background-color: rgb(227, 0, 43); border-radius: 10px')
        self.check_out_label.setAlignment(Qt.AlignCenter)

        self.phone_label = QLabel(self.central_widget)
        self.phone_label.setGeometry(1000, 750, 150, 40)
        self.phone_label.setText("<font color = 'white'>Phone number </font>")
        self.phone_label.setStyleSheet('background-color: rgb(227, 0, 43); border-radius: 10px')
        self.phone_label.setAlignment(Qt.AlignCenter)


        self.check_out_label_1 = QLabel(self.central_widget)
        self.check_out_label_1.setGeometry(800, 825, 150, 40)
        self.check_out_label_1.setStyleSheet('background-color: white; border-radius: 10px')
        self.check_out_label_1.setAlignment(Qt.AlignCenter)

        self.phone_label_1 = QLabel(self.central_widget)
        self.phone_label_1.setGeometry(1000, 825, 150, 40)
        self.phone_label_1.setStyleSheet('background-color: white; border-radius: 10px')
        self.phone_label_1.setAlignment(Qt.AlignCenter)
        

        red_background_bottom = RedBackgroundBottom(self.central_widget)

        self.retranslateUI()
        QMetaObject.connectSlotsByName(self.central_widget)
        main.setCentralWidget(self.central_widget)

    def retranslateUI(self):
        default_string = DefaultString.getDefaultString()

      
    def stopComponentsRunning(self):
        pass

    def listview_clicked(self):
        item = self.list_view.currentItem()
        temp = Data.DATA[str(item.text())]
        try:
            self.name_label_1.setText(self.result[temp]['user_id'])
            
        except:
            self.name_label_1.setText('')
 
        try:
            self.phone_label_1.setText(self.result[temp]['phone_number'])
        except:
            self.phone_label_1.setText('') 

        try:
            self.plate_label_1.setText(self.result[temp]['plate_number'])
        except:
            self.plate_label_1.setText('')

        try:
            self.check_in_label_1.setText(self.result[temp]['check_in_time'])
        except:
            self.check_in_label_1.setText('')

        try:
            self.check_out_label_1.setText(self.result[temp]['check_out_time'])
        except:
            self.check_out_label_1.setText('')
        
        try:
            self.date_label_1.setText(self.result[temp]['date'])
        except:
             self.date_label_1.setText('')

        try:
            self.customer_label_1.setText(self.result[temp]['key_lock_number'])
        except:
            self.customer_label_1.setText('')
        
        try:
            self.door_label_1.setText(self.result[temp]['door_status'])
        except:
            self.door_label_1.setText('')
        
    def backToSignIn(self):
        self.__main.onTransferScreen("startScreenLogin")

    def reloadData(self):
        self.result = self.firebase.get('Customer/', '') 
        for n in self.result:
            if n not in self.arr :
                self.list_view.addItem(self.result[n]['name'])
                self.arr.append(n)

        for p in self.arr:
            if p not in self.result:
                self.list_view.takeItem(self.arr.index(p))
                self.arr.remove(p)
            
    

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