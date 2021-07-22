import json
import requests
from requests.exceptions import ConnectionError
class ParseJson():
    def parse_json(self,qr_code):

        try:
           x = requests.get('https://autoklinikka-267610.appspot.com/bookings/QRCode/'+qr_code, timeout =10)
           

           return x.json()
        except ConnectionError:
            
            return 'ConnectionError'
    