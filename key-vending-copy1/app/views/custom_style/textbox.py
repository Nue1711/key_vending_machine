from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QGridLayout, QWidget, QLineEdit
from PyQt5.QtGui import QPixmap, QMovie, QIcon, QFont, QFontMetrics
from PyQt5.QtCore import QRect, Qt, pyqtSignal, QSize

class TextBox(QLineEdit):
    """ Screen title
    """

    def __init__(self, *args, **kwargs):
        QLineEdit.__init__(self, *args, **kwargs)

        self.__width_parent = self.parent().size().width()
        self.__height_parent = self.parent().size().height()

      
        self.__height = int(self.__height_parent * 0.15)
        self.__y = int(self.__height_parent * 0.40)
        
       
        self.setGeometry(QRect(0, self.__y, self.__width_parent, self.__height + 15))
        self.setAlignment(Qt.AlignCenter)
        
    def setXY(self, x, y,w, h):
            self.setGeometry(QRect(x, y, w, h))

    def setHeight(self, height):
        self.setFixedHeight(height)


