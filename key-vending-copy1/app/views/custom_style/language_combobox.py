from PyQt5.QtWidgets import QComboBox, QListView, QItemDelegate, QStyle, QStyledItemDelegate
from PyQt5.QtGui import QFont, QFontMetrics, QStandardItem, QColor, QPen, QBrush
from PyQt5.QtCore import QRect, Qt, pyqtSignal, QSize

class LanguageComboBox(QComboBox):
    """ Language combo box
    """

    on_language_changed = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        QComboBox.__init__(self, *args, **kwargs)

        width_parent = self.parent().size().width()
        height_parent = self.parent().size().height()
        
        width = int(80)
        height = int(45)
        x = int(width_parent - width - 50)
        y = int(height_parent * 0.04)

        self.setGeometry(QRect(x, y, width, height))
        
        self.__font = QFont()
        self.__font.setStyleStrategy(QFont.PreferAntialias)
        self.__font.setPixelSize(25)
        self.setFont(self.__font)

        # self.setStyleSheet("color: #000; background: transparent;")  

        self.setStyleSheet("QComboBox::item {\
                        font-size: 20pt;\
                        height: 60px;\
                        margin-top: 0px;\
                        margin-bottom: 0px;\
                        padding: 4px;\
                        padding-left: 18px;}\
                        QComboBox {\
                            background: #BF001B;\
                            color: #CCCCCC;\
                            outline: none;\
                            border-color: transparent;\
                        }\
                        ")

        # self.__list_view = QListView(self)
        # self.__list_view.setStyleSheet(" \
        #                     QListView::item {\
        #                                     height: 50px;}")
        # self.setView(self.__list_view)

        # model = self.model()
        # for row in range(2):
        #     item = QStandardItem(str(row))
        #     font = item.font()
        #     font.setPointSize(25)
        #     item.setFont(font)
        #     model.appendRow(item)

        self.addItem("FI")
        self.addItem("EN")

        self.activated[str].connect(self.__onChanged)  
        # self.setItemDelegate(LanguageDelegate())

    def __onChanged(self, text):
        self.on_language_changed.emit(text) 

    def setData(self, data: list):
        for item in data:
            self.addItem(item)

class LanguageDelegate(QStyledItemDelegate):
    """ Language delegate
    """

    def __init__(self, parent=None, *args):
        QStyledItemDelegate.__init__(self, parent, *args)
        self.font = QFont()
        self.font.setPointSize(30)
    
        # self.sizeHint().setHeight(60)
    
    def sizeHint(self, option, index):
        return QSize(100,60)

    def paint(self, painter, option, index):
        painter.save()

        # set background color
        painter.setPen(QPen(Qt.NoPen))
        if option.state & QStyle.State_Selected:
            # set background item when clicked
            painter.setBrush(QBrush(QColor("#fff")))
            # painter.setFont(self.font)
            pass

        # else:
            # painter.setBrush(QBrush(Qt.white))
        painter.drawRect(option.rect)

        # set text color
        painter.setPen(QPen(QColor("#000")))
        # value = index.data(Qt.DisplayRole)
        # if value.isValid():
        #     text = value.toString()
            
        #     painter.drawText(option.rect, Qt.AlignCenter, text)

        painter.restore()



            
