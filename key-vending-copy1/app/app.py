# ====================================================
# Created By : 
# Created Date : 
# ====================================================
# Application Name: Self-Service Kiosk (Autoklinikka)
# Version Application: 1.0.0
# Update Date:
# ====================================================
# Version Python:                                3.6.8
# Version PyQt:                            PyQt5-5.9.2
# Operation OS:                       Ubuntu 16.04 LTS
# ====================================================

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont
from model.user import User
from controllers.main_controller import MainController
from views.main_view import MainView
from constant.language import Language

class App(QApplication):
    def __init__(self, sys_argv): 
        super(App, self).__init__(sys_argv)
        
        # Language.setLanguage(Language.FI)

        self.width = self.primaryScreen().size().width()
        self.height = self.primaryScreen().size().height()
        self.build_settings = {'app_name': 'Autoklinikka', 'author': 'Trung Tran', 'version': '0.0.1', 'environment': 'local'}

        self.main_controller = MainController()
        self.main_view = MainView(self, self.build_settings, self.main_controller)
        self.main_view.showUI()
        #self.main_view.showUIFullScreen()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())



# enable when build file .exe
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel
# from PyQt5.QtGui import QFont
# from constant.path import Path
# from model.user import User
# from controllers.main_controller import MainController
# from views.main_view import MainView
# from fbs_runtime.application_context.PyQt5 import ApplicationContext
# import subprocess

# class App(ApplicationContext):           
#     def run(self):                              
#         if self.build_settings == None:
#             self.build_settings = {'app_name': 'SnapRentalsKiosk', 'author': 'Duc Nguyen', 'version': '0.0.1', 'environment': 'local'}

#         self.main_controller = MainController()
#         self.main_view = MainView(self, self.build_settings, self.main_controller)
#         self.main_view.showUI()
#         return self.app.exec_()

#     def copyShortcutToStartUpFolder(self):
#         try:
#             subprocess.Popen(Path.PATH_FOLDER + '\\app\\autostart.bat', shell=True)
#         except Exception as ex:
#             print(ex)
        

# if __name__ == '__main__':
#     appctxt = App()                      
#     exit_code = appctxt.copyShortcutToStartUpFolder()                   
#     exit_code = appctxt.run()                   
#     sys.exit(exit_code)
