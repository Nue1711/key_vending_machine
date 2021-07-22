from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap, QMovie, QIcon, QFont, QFontMetrics
from PyQt5.QtCore import QRect, Qt, pyqtSignal, QSize

class ScreenTitle(QLabel):
    """ Screen title
    """

    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)

        self.__width_parent = self.parent().size().width()
        self.__height_parent = self.parent().size().height()

        self.setStyleSheet("color: #000;\
                            font-weight: bold;")        

        self.__height = int(self.__height_parent * 0.15)
        self.__y = int(self.__height_parent * 0.40)
        
        self.__font = QFont()
        self.__font.setStyleStrategy(QFont.PreferAntialias)
        self.__font.setPixelSize(self.__height)
        self.setFont(self.__font)
        self.__fontMetrics = QFontMetrics(self.__font)
        width_text = self.__fontMetrics.width(self.text())
        height_text = self.__fontMetrics.height()
        # self.__height = height_text * 1.7
        self.setGeometry(QRect(0, self.__y, self.__width_parent, self.__height + 15))
        self.setAlignment(Qt.AlignCenter)
        self.setWordWrap(True)

       
    def setTextSize(self, size):
        self.__font.setPixelSize(size)
        self.setFont(self.__font)
        width_text = self.__fontMetrics.width(self.text())
        height_text = self.__fontMetrics.height()

    def setXY(self, x, y):
        self.setGeometry(QRect(x, y, self.__width_parent, self.__height + 15))

    def setHeight(self, height):
        self.setFixedHeight(height)

class NormalText(QLabel):
    """ Normal text
    """

    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)

        self.__width_parent = self.parent().size().width()
        self.__height_parent = self.parent().size().height()

        self.setStyleSheet("color: #000;\
                            font-weight: 0;")        

        self.__height = int(self.__height_parent * 0.07)
        self.__y = int(self.__height_parent * 0.7)
        
        self.__font = QFont()
        self.__font.setStyleStrategy(QFont.PreferAntialias)
        self.__font.setPixelSize(self.__height)
        self.setFont(self.__font)
        self.__fontMetrics = QFontMetrics(self.__font)
        width_text = self.__fontMetrics.width(self.text())
        height_text = self.__fontMetrics.height()

        self.setGeometry(QRect(0, self.__y, self.__width_parent, self.__height + 15))
        self.setAlignment(Qt.AlignCenter)
        self.setWordWrap(True)

    def setTextSize(self, size):
        self.__font.setPixelSize(size)
        self.setFont(self.__font)
        width_text = self.__fontMetrics.width(self.text())
        height_text = self.__fontMetrics.height()
        self.setGeometry(QRect(0, self.__y, self.__width_parent, self.__height + 15))

    def setXY(self, x, y):
        self.setGeometry(QRect(x, y, self.__width_parent, self.__height + 15))

    def setHeight(self, height):
        self.setFixedHeight(height)

class ConnectionErrorText(QLabel):
    """ ConnectionErrorText
    """

    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)

        self.__width_parent = self.parent().size().width()
        self.__height_parent = self.parent().size().height()

        self.setStyleSheet("color: red;\
                            font-weight: 0;")        

        self.__height = int(self.__height_parent * 0.03)
        self.__y = int(self.__height_parent * 0.9)
        
        self.__font = QFont()
        self.__font.setStyleStrategy(QFont.PreferAntialias)
        self.__font.setPixelSize(self.__height)
        self.setFont(self.__font)
        self.__fontMetrics = QFontMetrics(self.__font)
        width_text = self.__fontMetrics.width(self.text())
        height_text = self.__fontMetrics.height()

        self.setGeometry(QRect(0, self.__y, self.__width_parent, self.__height + 15))
        self.setAlignment(Qt.AlignCenter)
        self.setWordWrap(True)

class CustomText(QLabel):
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)

        width_parent = self.parent().size().width()
        height_parent = self.parent().size().height()
        
        text_size = int(height_parent / 9)
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        font.setPixelSize(text_size)

        self.setStyleSheet("color: #000;")
        self.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.setFont(font)
    
    def setAlignRight(self):
        self.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

class LogoApp(QLabel):
    """ Logo app
    """

    def __init__(self, icon_path, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)

        width_parent = self.parent().size().width()
        height_parent = self.parent().size().height()
        
        width = int(width_parent * 0.5)
        height = int(height_parent * 0.2)
        x = int((width_parent - width)/2)
        y = int(height_parent * 0.04)

        self.setGeometry(QRect(x, y, width, height))
        
        self.setScaledContents(True)
        self.setPixmap(QPixmap(icon_path))

class RedBackgroundTop(QLabel):
    """ Red background top
    """

    def __init__(self, icon_path, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)

        width_parent = self.parent().size().width()
        height_parent = self.parent().size().height()
        height = int(height_parent * 0.12)

        self.setGeometry(QRect(0, 0, width_parent, height))
        self.setStyleSheet("background: #E3002B;")
        
        width_icon = int(width_parent * 0.25)
        height_icon = int(height * 0.9)
        icon = QLabel(self)
        icon.setGeometry(QRect(int(height * 0.1), int(height * 0.05), width_icon, height_icon))
        icon.setScaledContents(True)
        icon.setPixmap(QPixmap(icon_path))

class RedBackgroundBottom(QLabel):
    """ Red background bottom
    """

    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)

        width_parent = self.parent().size().width()
        height_parent = self.parent().size().height()
        height = int(height_parent * 0.02)
        y = height_parent - height

        self.setGeometry(QRect(0, y, width_parent, height))
        self.setStyleSheet("background: #E3002B;")

class GifImage(QWidget):
    """ Image gif
    https://www.flaticon.com/free-icon/right_1635581?term=arrow%20right&page=1&position=22
    """
    def __init__(self, icon_path, parent = None):
        super(QWidget, self).__init__(parent)

        width_parent = self.parent().size().width()
        height_parent = self.parent().size().height()

        width = int(width_parent * 0.64)
        height = int(height_parent * 0.4)
        x = int((width_parent - width)/2)
        y = int(height_parent * 0.32)
        w = QWidget(self)
        w.setGeometry(QRect(x, y, width, height))
        # w.setStyleSheet("background: #fff123;")

        qr_width = int(width * 0.2)
        qr_height = qr_width
        qr_y = int((height - qr_height) / 2)
        self.qr_icon = QLabel(w)
        self.qr_icon.setGeometry(QRect(0, qr_y, qr_width, qr_height))
        self.qr_icon.setScaledContents(True)
        self.qr_icon.setPixmap(QPixmap(icon_path + '/icon/qr.png'))
        
        arrow_width = int(width * 0.25)
        arrow_height = int(height * 0.25)
        arrow_x = qr_width + int(width * 0.1)
        arrow_y = int((height - arrow_height) / 2)
        self.arrow_icon = QLabel(w)
        self.arrow_icon.setGeometry(QRect(arrow_x, arrow_y, arrow_width, arrow_height))
        self.arrow_icon.setScaledContents(True)
        self.arrow_icon.setPixmap(QPixmap(icon_path + '/icon/arrow_right.png'))

        self.gif_icon = QLabel(w)
        self.gif_movie = QMovie(icon_path + '/gif/scan_qr.gif')
        self.gif_icon.setAlignment(Qt.AlignCenter)
        self.gif_icon.setScaledContents(True)
        self.gif_icon.setMovie(self.gif_movie)

        gif_width = height
        gif_height = gif_width
        gif_x = int((width - gif_width))
        self.gif_icon.setGeometry(QRect(gif_x, 0, gif_width, gif_height))

    def startGif(self):
        self.gif_movie.start()

    def stopGif(self):
        self.gif_movie.stop()

    def setXY(self, x, y):
        self.setGeometry(QRect(x, y, self.__width_parent, self.__height))
    

class Text(QLabel):
    """ Screen title
    """

    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)

        self.__width_parent = self.parent().size().width()
        self.__height_parent = self.parent().size().height()

        self.setStyleSheet("color: #000;\
                            font-weight: 0;")        

        self.__height = int(self.__height_parent * 0.15)
        self.__y = int(self.__height_parent * 0.40)
        
        self.__font = QFont()
        self.__font.setStyleStrategy(QFont.PreferAntialias)
        self.__font.setPixelSize(self.__height)
        self.setFont(self.__font)
        self.__fontMetrics = QFontMetrics(self.__font)
        width_text = self.__fontMetrics.width(self.text())
        height_text = self.__fontMetrics.height()
        # self.__height = height_text * 1.7
        self.setGeometry(QRect(0, self.__y, self.__width_parent, self.__height + 15))
        self.setAlignment(Qt.AlignCenter)
        self.setWordWrap(True)

    def setTextSize(self, size):
        self.__font.setPixelSize(size)
        self.setFont(self.__font)
        width_text = self.__fontMetrics.width(self.text())
        height_text = self.__fontMetrics.height()

    def setXY(self, x, y):
        self.setGeometry(QRect(x, y, self.__width_parent, self.__height + 15))

    def setHeight(self, height):
        self.setFixedHeight(height)
    
    def setStartHidden(self):
        self.setHidden(True)
    def setStopHidden(self):
        self.setHidden(False)    
    
class LogoApp1(QLabel):
    """ Logo app
    """

    def __init__(self, icon_path, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)

        width_parent = self.parent().size().width()
        height_parent = self.parent().size().height()

        print(width_parent)
        print(height_parent)
        
        width = int(width_parent * 0.3)
        height = int(height_parent * 0.3)
        x = int((width_parent - width)/2)
        y = int(height_parent * 0.2)

        self.setGeometry(QRect(x, y, width, height))
        print(x)
        print(y)
        self.setScaledContents(True)
        self.setPixmap(QPixmap(icon_path))
