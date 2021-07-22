import face_recognition
import cv2
import numpy as np
from views import face_Recognition
from PyQt5.QtCore import pyqtSignal, QThread,QObject
from model.user import User
import time
from constant.path import Path
import os
from firebase import firebase
import pickle


class FaceRec(): 
 
  def __init__(self,user,main):
      self.__user = user
      self.__main = main
      self.known_face_names = []
      self.known_face_encodings = []
      
      
      self.firebase = firebase.FirebaseApplication("https://test-60f7d-default-rtdb.firebaseio.com/", None)
      self.result = self.firebase.get('Customer/' + self.__user.user_id, '')
      print(self.result['name'])
      
      
      for users in os.listdir(Path.PATH_IMAGE):
      	self.known_face_names.append(users)
      print(self.known_face_names)

      with open('/home/trung1711/Pictures/key-vending-copy1/app/resources/dataset_faces.dat', 'rb') as f:
          self.all_face_encodings = pickle.load(f)

      self.known_face_names = list(self.all_face_encodings.keys())
      self.known_face_encodings = np.array(list(self.all_face_encodings.values()))
      print(self.known_face_names)	
      
      
  def face_rec(self,frame):
      self.__frame = frame 
      small_frame = cv2.resize(self.__frame, (0, 0), fx=0.25, fy=0.25)
      rgb_frame = small_frame[:, :, ::-1]
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
      
    
      face_locations = face_recognition.face_locations(rgb_frame)
      face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

      for face_encoding in (face_encodings):
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                  if self.known_face_names[best_match_index] != self.result['name']:
                    self.__user.qr_code = False
                  else:
                    self.__user.qr_code = True    
                    self.__user.name = self.known_face_names[best_match_index] 
                    print(self.result['phone_number']) 
                    print(self.result['plate_number'])
                    self.__user.phone_number = self.result['phone_number']
                    self.__user.plate_number = self.result['plate_number'] 
                    print(self.__user.name)
                else:
                  self.__user.qr_code = False
                  print(self.__user.qr_code)

  
    

