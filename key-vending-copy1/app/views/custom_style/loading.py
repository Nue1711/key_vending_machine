from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtCore import Qt, QRect
from views.custom_style.spinner import WaitingSpinner

class Loading(QWidget):
    """ Loading
    """
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        
        w = QWidget(self)
        w.setGeometry(QRect(0, 0, 1280,768))


        w.setStyleSheet("background-color: rgba(0, 0, 0, 30%);")

        self.__spinner = WaitingSpinner(w, radius=20, line_length=25, line_width=3)
        self.setHidden(True)

    def startLoading(self):
        self.setHidden(False)
        self.__spinner.start()
    
    def stopLoading(self):
        if self.__spinner:
            self.setHidden(True)
            self.__spinner.stop()