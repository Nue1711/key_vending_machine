import cv2
import datetime
import time
import os

class CaptureWebcam:
    """ Capture webcam
        
        Capture and save file image from webcam
        
        Attributes:
            nameImage: image name is saved
            path:
    """

    __nameImage = 'image_webcam'
    __isCapture = False
    __fullNameImage = ''

    def __init__(self, nameImage, path):
        self.path = path
        self.__nameImage = nameImage
        self.__isCapture = False

    def captureImage(self, deviceIndex):
        """ Capture Image
        
            Capture and save file image from webcam
            
            Attributes:
                deviceIndex: port webcam
            Returns:
                The frame image from webcam
        """
        # create camera with index device
        camera = cv2.VideoCapture(deviceIndex)

        # set width height frame image
        camera.set(3,1280)
        camera.set(4,720)
        
        # wait camera stability in 2 seconds
        time.sleep(2)

        # if capture successful -> return_value = true
        (return_value, image) = camera.read()

        # check capture successful or fail
        if not return_value:
            print('Not connect to webcam')
        else:
            # yyyy_mm_dd_hh_mm_ss
            now = datetime.datetime.now()
            day = '_' + str(now.year) + '_' + str(now.month) + '_' + str(now.day) + '_'   
            inday = str(now.hour) + '_' + str(now.minute) + '_' + str(now.second)

            # create Image folder -> write image
            if not os.path.exists(self.path):
                os.makedirs(self.path)

            self.__fullNameImage = str(self.__nameImage) + day + inday + '.png'

            # write image to path
            cv2.imwrite(os.path.join(self.path, self.__fullNameImage), image)
            
            self.__isCapture = True
            
            # destroy camera
            del(camera)

            return image

    def getNamecaptureImage(self):
        return self.__fullNameImage

    def isSuccessfulCapture(self):
        return self.__isCapture

    
        

