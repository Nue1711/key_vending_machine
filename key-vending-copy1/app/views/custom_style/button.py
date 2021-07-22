from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QMovie, QIcon, QFont, QFontMetrics
from PyQt5.QtCore import QRect, Qt, pyqtSignal, QSize

class NextButton(QPushButton):
    """ Next page button

        Attributes:
            path: path icon
    """

    def __init__(self, icon_path, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        
        self.__width_parent = self.parent().size().width()
        self.__height_parent = self.parent().size().height()
        
        self.__width = int(self.__width_parent * 0.1)
        self.__height = int(self.__height_parent * 0.1)
        self.__x = int((self.__width_parent - self.__width)/2)
        self.__y = int(self.__height_parent * 0.65)

        self.setGeometry(QRect(self.__x, self.__y, self.__width, self.__height))
        
        self.setStyleSheet("QPushButton {\
                                background-color: rgb(227, 0, 43);\
                                border-radius: 10px;\
                                font-weight:400;\
                                color: rgb(255,255,255);\
                                padding-right: 30px;\
                                outline: none;}" 
                            "QPushButton:pressed {\
                                padding-right: 30px;\
                                background-color: rgba(227, 0, 43, 80%);\
                                border-radius: 10px;}")
        self.setText("Next")

        self.__font = QFont()
        self.__font.setStyleStrategy(QFont.PreferAntialias)
        self.__font.setPixelSize(30)
        self.setFont(self.__font)

        self.__width_icon = int(self.__width * 0.3)
        self.__height_icon = int(self.__height * 0.6)
        self.__x_icon = int(self.__width - self.__width_icon)
        self.__y_icon = int(self.__height * 0.2)

        self.icon = QLabel(self)
        self.icon.setGeometry(QRect(self.__x_icon, self.__y_icon, self.__width_icon, self.__height_icon))
        self.icon.setScaledContents(True)
        self.icon.setPixmap(QPixmap(icon_path))
        self.icon.setStyleSheet("background-color: transparent;")

    def setTextSize(self, size):
        self.__font.setPixelSize(size)
        self.setFont(self.__font)

    def setXY(self, x, y, w, h):
        self.setGeometry(QRect(x, y, w, h))

    def setSize(self, width):
        self.setFixedWidth(width)
        
        self.__x_icon = int(width - self.__width_icon)
        
        self.icon.setGeometry(QRect(self.__x_icon, self.__y_icon, self.__width_icon, self.__height_icon))
        
        self.__x = int((self.__width_parent - width)/2)
        print('xx: ', self.__x)
        
        self.setGeometry(QRect(self.__x -15, self.__y + 70, self.__width, self.__height))

        

    def setWidth(self, width):
        self.setFixedWidth(width)
        
        self.__x_icon = int(width - self.__width_icon)
        
        self.icon.setGeometry(QRect(self.__x_icon, self.__y_icon, self.__width_icon, self.__height_icon))
        
        self.__x = int((self.__width_parent - width)/2)
        
        self.setGeometry(QRect(self.__x, self.__y, self.__width, self.__height))


class StartButton(QPushButton):
    """ start button

        Attributes:
            path: path icon
    """

    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        
        self.__width_parent = self.parent().size().width()
        self.__height_parent = self.parent().size().height()
        
        self.__width = int(self.__width_parent * 0.3)
        self.__height = int(self.__height_parent * 0.2)
        self.__x = int((self.__width_parent - self.__width)/2)
        self.__y = int(self.__height_parent * 0.6)

        self.setGeometry(QRect(self.__x, self.__y, self.__width, self.__height))
        
        self.setStyleSheet("QPushButton {\
                                background-color: rgb(227, 0, 43);\
                                border-radius: 20px;\
                                font-weight:500;\
                                color: rgb(255,255,255);\
                                outline: none;}" 
                            "QPushButton:pressed {\
                                background-color: rgba(227, 0, 43, 80%);\
                                border-radius: 20px;}")
        self.setText("START")

        self.__font = QFont()
        self.__font.setStyleStrategy(QFont.PreferAntialias)
        self.__font.setPixelSize(60)
        self.setFont(self.__font)

    def setTextSize(self, size):
        self.__font.setPixelSize(size)
        self.setFont(self.__font)

    def setXY(self, x, y, w, h):
        self.setGeometry(QRect(x, y, w, h))

    def setWidth(self, width):
        self.setFixedWidth(width)
        
        self.__x_icon = int(width - self.__width_icon)
        
        self.icon.setGeometry(QRect(self.__x_icon, self.__y_icon, self.__width_icon, self.__height_icon))
        
        self.__x = int((self.__width_parent - width)/2)
        
        self.setGeometry(QRect(self.__x , self.__y, self.__width, self.__height))
