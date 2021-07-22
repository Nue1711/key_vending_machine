from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage, QPainter
import cv2
from views.face_rec import FaceRec
import face_recognition

class PreviewWebcamWidget(QWidget):
    """ Preview webcam widget
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.image = QImage()
        self._red = (0, 0, 255)
        self._width = 2
        self._min_size = (30, 30)
        

    def imageDataSlot(self, image_data):
      
      self.image = self.getImage(image_data)
      if self.image.size() != self.size():
         self.setFixedSize(self.image.size())
      
      self.update()
      

      
    def getImage(self, image):
        """ Convert frame image to QImage 
        """
        height, width, colors = image.shape
        bytesPerLine = 3 * width
        Image = QImage

        image = Image(image.data,
                       640,
                       380,
                       bytesPerLine,
                       Image.Format_RGB888)
        image = image.rgbSwapped()
        return image

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QImage()