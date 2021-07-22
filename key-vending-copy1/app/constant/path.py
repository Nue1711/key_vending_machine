import sys
import os
pathFolder = os.getcwd()
sys.path.append(pathFolder)

class Path():
    """ Path folders

        Attributes:
            PATH_FOLDER: path main folder 
            PATH_ICON: path icon image
            PATH_IMAGE_CAPTURE: path image capture webcam
            PATH_IMAGE_DOWNLOAD = path image download
            PATH_RESOURC: path resource file
    """
    PATH_FOLDER = pathFolder
    PATH_ICON = pathFolder + '/app/resources/icon'
    PATH_IMAGE_CAPTURE = pathFolder + '/app/resources/ImageCapture'
    PATH_IMAGE_DOWNLOAD = pathFolder + '/app/resources/img'
    PATH_RESOURCE = pathFolder + '/app/resources'
    PATH_IMAGE = pathFolder + '/app/resources/dataset'
    PATH_PARENT = pathFolder + '/app/resources/dataset/'
