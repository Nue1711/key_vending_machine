import random
from firebase import firebase
class Data():
   
    DATA = {}
    fire = firebase.FirebaseApplication("https://test-60f7d-default-rtdb.firebaseio.com/", None)
    result = fire.get('Customer/', '')
    for keys in result:
        DATA[result[keys]['name']] = keys
   
    KEY_LOCK_NUMBER = []
    for n in result:
        KEY_LOCK_NUMBER.append(result[n]['key_lock_number'])
  