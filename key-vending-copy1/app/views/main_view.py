from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.QtCore import Qt, pyqtSignal, QCoreApplication
from PyQt5.QtGui import QKeyEvent, QKeySequence

from controllers.welcome_controller import WelcomeController
from controllers.login_controller import LoginController
from controllers.add_name_controller import AddNameController
from controllers.sign_up_controller import SignUpController
from controllers.sign_in_controller import SignInController
from controllers.admin_controller import AdminController
from controllers.training_face_controller import TrainingFaceController
from controllers.wait_training_controller import WaitTrainingController
from controllers.wait_qr_code_controller import WaitQRCodeController
from controllers.scan_qr_controller import ScanQRController
from controllers.scan_true_qr_controller import ScanTrueQRController
from controllers.scan_not_true_controller import ScanNotTrueQRController
from controllers.close_door_controller import CloseDoorController
from controllers.thank_you_controller import ThankYouController
from controllers.thank_another_controller import ThankAnotherController
from controllers.scan_another_true_qr_controller import ScanAnotherTrueController
from controllers.pick_up_key_controller import PickUpKeyController
from controllers.drop_key_controller import DropKeyController
from controllers.connection_error_controller import ConnectionErrorController
from controllers.full_lock_controller import FullLockController
from controllers.take_key_controller import TakeKeyController


from views.welcome_view import WelcomeView
from views.login_view import LoginView
from views.add_name_view import AddNameView
from views.training_face_view import TrainingFaceView
from views.sign_up_view import SignUpView
from views.sign_in_view import SignInView
from views.admin_view import AdminView
from views.wait_training_view import WaitTrainingView
from views.wait_qr_code_view import WaitQRCodeView
from views.scan_qr_view import ScanQRView
from views.scan_qr_true_view import ScanQRTrueView
from views.scan_qr_not_true_view import ScanQRNotTrueView
from views.close_door_view import CloseDoorViewView
from views.thank_you_view import ThankYouViewView
from views.thank_another_view import ThankYouAnotherView
from views.scan_qr_another_true_view import ScanQRAnotherTrueView
from views.pick_up_key_view import PickUpKeyView
from views.drop_key_view import DropKeyView
from views.connection_error_view import ConnectionErrorView
from views.full_lock_view import FullLockView
from views.take_key_view import TakeKeyView


from utils.write_log import writeExceptionToFile, writeExecutionSteps
from model.user import User

from utils.observable_trigger import ObservableTrigger
from controllers.parse_json import ParseJson
obs = ObservableTrigger.getInstance()

class MainView(QMainWindow):
    onCloseApp = pyqtSignal()
    __hardware_error = pyqtSignal()

    def __init__(self, app, build_settings, controller):
        super(MainView, self).__init__()
        self.__registerListenerEvent()

        self.parsejson = ParseJson()

        self.is_start_session = True
        writeExecutionSteps(header="Open")

        self.width = app.width
        self.height = app.height

        self.__build_settings = build_settings
        self.__controller = controller
        self.__app = app
        self.__current_screen = None
        self.__is_hardware_error = False
        self.keylist = []
        # initial config Main Window
        self.__initial()

        self.__screen_dispatcher = {
            "startScreenWelcome" : self.__startScreenWelcome,
            "startScreenWaitQRCode" : self.__startScreenWaitQRCode,
            "startScreenScanQR" : self.__startScreenScanQR,
            "startScreenScanQRTrue": self.__startScreenScanQRTrue,
            "startScreenLogin": self.__startScreenLogin,
            "startScreenAddName": self.__startScreenAddName,
            "startScreenTrainingFace" : self.__startScreenTrainingFace,
            "startScreenSignUp": self.__startScreenSignUp,
            "startScreenSignIn": self.__startScreenSignIn,
            "startScreenAdmin": self.__startScreenAdmin,
            "startScreenFullLock": self.__startScreenFullLock,
            "startScreenWaitTraining": self.__startScreenWaitTraining,
            "startScreenScanQRNotTrue": self.__startScreenScanQRNotTrue,
            "startScreenCloseDoor":self.__startScreenCloseDoor,
            "startScreenThankYou":self.__startScreenThankYou,
            "startScreenThankAnother":self.__startScreenThankAnother,
            "startScreenScanQRAnotherTrue": self.__startScreenScanQRAnotherTrue,
            "startScreenPickUpKey":self.__startScreenPickUpKey,
            "startScreenDropKey":self.__startScreenDropKey,
            "startScreenConnectionError":self.__startScreenConnectionError,
            "startScreenTakeKey": self.__startScreenTakeKey
            

        }

        self.__user = User()
        #self.__startScreenTrainingFace()
        self.__startScreenWelcome()
        #self.__startScreenTakeKey()
        #self.__startScreenAddName()
        #self.__startScreenAdmin()
        #self.__startScreenSignUp()
        # self.__startScreenWaitQRCode()
        #self.__startScreenScanQR()
        #self.__startScreenScanQRTrue()
        #self.__startScreenScanQRNotTrue()
        #self.__startScreenWaitTraining()

    def __registerListenerEvent(self):
        self.registerExitAppListener()
    
    def __removeListenerEvent(self):
        obs.off()

    def onTransferScreen(self, screen, option=None):
        try:
            if self.__is_hardware_error:
                return
                
            if (screen.__contains__("startScreenThankYou") or 
               screen.__contains__("startScreenThankYouInform")):
                self.is_start_session = False
            
            if option == None:
                self.__screen_dispatcher[screen]()
            else:
                self.__screen_dispatcher[screen](option)
        except Exception as err:
            print (err)

    def __initial(self):
        version = self.__build_settings['version']
        app_name = self.__build_settings['app_name']
        self.setWindowTitle(app_name + " - v" + version)
        # self.resize(1280,800)
        # self.setFixedSize(self.width, self.height)
        self.setWindowFlags(
            Qt.Window |
            Qt.CustomizeWindowHint |
            Qt.WindowTitleHint |
            Qt.WindowCloseButtonHint |
            Qt.WindowStaysOnTopHint |  
            Qt.FramelessWindowHint
        )
        self.setStyleSheet("background: #fff;")

    def __resetValue(self):
        """ Reset value
        
            Reset some fields on default value

            Attributes:
                is_scanned_qr_code: True if qr_code exist value, can't scan anymore in the session
                is_uppercase_qr_code: True if still button SHIFT 
                user: create model contain information of the user
        """

        self.__user = User()
        self.__is_scanned_qr_code = False
        self.__is_uppercase_qr_code = False
        self.__qr_code = ''

        # self.__user.name = "Matti Meikalainen"
        # self.__user.vehicle = "XXX-101"
        # self.__user.reserved_time = "01.01.2020, 7:00AM"
        # self.__user.balance = "550,00€"

    def __startScreenWelcome(self):
        """ Start Screen welcome
        """      
        self.__resetValue()
        
        if self.is_start_session:
            writeExecutionSteps(header="Start")
            self.is_start_session = False
        else:
            writeExecutionSteps(header="Finish")
            writeExecutionSteps(header="Start")

        self.__current_controller = WelcomeController(self.__user)
        self.__current_screen = WelcomeView(self.__user, self.__current_controller, self)

    def __startScreenAdmin(self):
        self.__current_controller = AdminController(self.__user)
        self.__current_screen = AdminView(self.__user, self.__current_controller, self)
    
    def __startScreenFullLock(self):
        self.__current_controller = FullLockController(self.__user)
        self.__current_screen = FullLockView(self.__user, self.__current_controller, self)
    
    def __startScreenTakeKey(self):
        self.__current_controller = TakeKeyController(self.__user)
        self.__current_screen = TakeKeyView(self.__user, self.__current_controller, self)

    def __startScreenAddName(self):
        """ Start Screen wait QR Code
        """      
        self.__current_controller = AddNameController(self.__user)
        self.__current_screen = AddNameView(self.__user, self.__current_controller, self)
    

    def __startScreenWaitTraining(self):
        """ Start Screen wait QR Code
        """      
        self.__current_controller = WaitTrainingController(self.__user)
        self.__current_screen = WaitTrainingView(self.__user, self.__current_controller, self)

    def __startScreenLogin(self):
        """ Start Screen wait QR Code
        """      
        self.__current_controller = LoginController(self.__user)
        self.__current_screen = LoginView(self.__user, self.__current_controller, self)
    

    def __startScreenTrainingFace(self):
        """ Start Screen Training Face
        """      
        self.__current_controller = TrainingFaceController(self.__user)
        self.__current_screen = TrainingFaceView(self.__user, self.__current_controller, self)
    
    def __startScreenSignUp(self):
        """ Start Screen SignUp
        """      
        self.__current_controller = SignUpController(self.__user)
        self.__current_screen = SignUpView(self.__user, self.__current_controller, self)
    
    def __startScreenSignIn(self):
        """ Start Screen SignIn
        """      
        self.__current_controller = SignInController(self.__user)
        self.__current_screen = SignInView(self.__user, self.__current_controller, self)

    def __startScreenWaitQRCode(self):
        """ Start Screen wait QR Code
        """      
        self.__current_controller = WaitQRCodeController(self.__user)
        self.__current_screen = WaitQRCodeView(self.__user, self.__current_controller, self)
        
    def __startScreenScanQR(self):
        """ Start scan QR Code
        """
        self.__is_scanned_qr_code = True
        self.__current_controller = ScanQRController(self.__user)
        self.__current_screen = ScanQRView(self.__user, self.__current_controller, self)
    
    def __startScreenScanQRTrue(self):
        self.__current_controller = ScanTrueQRController(self.__user)
     
        self.__current_screen = ScanQRTrueView(self.__user, self.__current_controller, self)
    def __startScreenScanQRNotTrue(self):
        self.__current_controller = ScanNotTrueQRController(self.__user)
        self.__current_screen = ScanQRNotTrueView(self.__user, self.__current_controller, self)

    def __startScreenCloseDoor(self):
        self.__current_controller = CloseDoorController(self.__user)
        self.__current_screen = CloseDoorViewView(self.__user, self.__current_controller, self)

    def __startScreenThankYou(self):
        self.__current_controller = ThankYouController(self.__user)
        self.__current_screen = ThankYouViewView(self.__user, self.__current_controller, self)
    
    def __startScreenThankAnother(self):
        self.__current_controller = ThankAnotherController(self.__user)
        self.__current_screen = ThankYouAnotherView(self.__user, self.__current_controller, self)

    def __startScreenScanQRAnotherTrue(self):
        self.__current_controller = ScanAnotherTrueController(self.__user)
        self.__current_screen = ScanQRAnotherTrueView(self.__user, self.__current_controller, self)

    def __startScreenPickUpKey(self):
        self.__current_controller = PickUpKeyController(self.__user)
        self.__current_screen = PickUpKeyView(self.__user, self.__current_controller, self)

    def __startScreenDropKey(self):
        self.__current_controller = DropKeyController(self.__user)
        self.__current_screen = DropKeyView(self.__user, self.__current_controller, self)
        
    def __startScreenConnectionError(self):
        self.__current_controller = ConnectionErrorController(self.__user)
        self.__current_screen = ConnectionErrorView(self.__user, self.__current_controller, self)

   
         
        
    def registerExitAppListener(self):
        self.shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut.activated.connect(self.exitApp)

    def exitApp(self):
        self.closeEvent('')
        QCoreApplication.quit()

    def closeEvent(self, event):
        try:
            self.onCloseApp.emit()
            self.__removeListenerEvent()
        except Exception:
            writeExceptionToFile()

        try:
            self.__controller.stopRemoteControl()
        except Exception:
            writeExceptionToFile()
            
        try:
            self.__controller.stopUpdateMachine()
        except Exception:
            writeExceptionToFile()
        
        try:
            self.__current_screen.stopComponentsRunning()
        except Exception:
            writeExceptionToFile()
    
    def stopCurrentScreenRunning(self):
        try:
            self.__controller.stopUpdateMachine()
        except Exception:
            writeExceptionToFile()

        try:
            self.__controller.stopRemoteControl()
        except Exception:
            writeExceptionToFile()

        try:
            self.__current_screen.stopComponentsRunning()
        except Exception:
            writeExceptionToFile()

    def showUI(self):
        self.show()

    def showUIFullScreen(self):
        self.showFullScreen()
    
    def qrCodeScanned(self):
        """ Scanned QR Code
        """
        writeExecutionSteps("QR Code: " + str(self.__qr_code))
        self.__is_scanned_qr_code = False
        #self.__user.qr_code ='WNYKX70HWVU4I5K07FGP'
        self.__user.qr_code ='M07FXOS8RZS3FDZ56S54' 
        
        

        self.__startScreenWaitQRCode()
    '''
    def keyPressEvent(self, event):
    
        if (self.__is_scanned_qr_code == False):            
            event.ignore()
            return

        if type(event) == QKeyEvent:
            #here accept the event and do something
            key = event.key()
            
            if(key >= Qt.Key_Space & key <= Qt.Key_AsciiTilde):
                
                if key == Qt.Key_Shift:
                    self.__is_uppercase_qr_code = True

                if (key < 0x01000000):
                    # if uppercase char
                    if self.__is_uppercase_qr_code:
                        self.__qr_code = self.__qr_code + chr(key)
                        self.__is_uppercase_qr_code = False
                    else:
                        # if barcode exist number 0-9 else lowercase char 
                        if key in range(32,58):
                            self.__qr_code = self.__qr_code + chr(key)
                        else:
                            self.__qr_code = self.__qr_code + chr(key+32)                                                           
                    event.accept()
                      
            if(key == Qt.Key_Return):
                event.accept()
                
                
                self.qrCodeScanned()
            
                
            else:
                event.ignore()
                   
            #else:
                #event.ignore()

        else:
            event.ignore()
    '''        
           