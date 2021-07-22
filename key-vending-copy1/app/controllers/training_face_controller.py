from PyQt5.QtCore import QObject, pyqtSlot,pyqtSignal
from utils.write_log import writeExceptionToFile
import face_recognition
class TrainingFaceController(QObject):
    get_qr_result = pyqtSignal(int)
    
    

    def __init__(self, user):
        super().__init__()
        self.__user =user
    '''
    @pyqtSlot()
    def requestQR(self):
        trung_image = face_recognition.load_image_file("michael-jordan.jpg")
        trung_face_encoding = face_recognition.face_encodings(trung_image)[0]
    

        known_face_encoding = [trung_face_encoding]
        known_face_name = ["Michael Jordan"]
        self.__thread_face_rec = ThreadFaceRec(known_face_encoding ,known_face_name)
        self.__thread_face_rec.request_qrCode.connect(self._getInfo)
        self.__thread_face_rec.start()
        print(self.__user.qr_code)
    
    @pyqtSlot(bool)
    def _getInfo(self):
        self.get_qr_result.emit(self.__user.qr_code)
    '''
