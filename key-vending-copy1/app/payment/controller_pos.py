# sudo minicom -D  /dev/ttyUSB3 -H --displayhex -w --wrap

from payment.break_status_pos import breakStatus
from datetime import datetime
import serial
import binascii
import time

from utils.observable_trigger import ObservableTrigger
obs = ObservableTrigger.getInstance()

ENQ = 0x05
ACK = 0x06
STX = 0x02
ETX = 0x03

class ControllerPOS:
    ''' Controller Point Of Sale
    '''

    def __init__(self, com_port=None, updateStatus=None):
        self.com_port = com_port
        self.__uart = None
        self.__is_stop = False
        self.__status_list = []
        self.updateStatus = updateStatus

    def initialize(self):
        self.__uart = serial.Serial(baudrate=19200)  # BR 19200, 8, N, 1
        self.__uart.port = self.com_port
        self.__uart.timeout = 1
        try:
            self.__uart.open()
            if self.__uart.isOpen():
                return True
            else:
                obs.trigger("hardwareError")
                return False
        except serial.serialutil.SerialException as error:
            obs.trigger("hardwareError")
            return False

    def isOpen(self):
        if not self.__uart.isOpen():
            obs.trigger("hardwareError")
        return self.__uart.isOpen()

    def calculateLCR(self, byte_array):
        lrc = 0x00
        for b in range(1,len(byte_array) - 2):
            lrc ^= byte_array[b]
        return lrc ^ 0x03

    def writeENQ(self):
        """ Write 0x05
        """
        self.__uart.write(bytes(b"\x05"))

        response = self.__uart.read()
        print (self.byteString2String(response))
        if self.byteString2String(response) == "06":
            print (self.byteString2String(response))
            return True
        return False

    def writeACK(self):
        """ Write 0x06
        """
        self.__uart.write(bytes(b"\x06"))

        response = self.__uart.read()
        print (self.byteString2String(response))
        if self.byteString2String(response) == "06":
            print (self.byteString2String(response))
            return True
        return False

    def readStatus(self, price, date, is_preauth):
        self.__status_list = []
        is_start= False	
        status = ""
        while not self.__is_stop:
            response = self.__uart.read()
            response = self.byteString2String(response)
            if response == "06":
                print ("0x06")
            if response == "02":
                is_start = True
                continue
            elif response == "03": 
                is_start = False	
                continue
            
            if is_start:
                status += response
            else:                    
                if status != "":      
                    status = bytes.fromhex(status).decode('utf-8')      
                    self.setStatus(status)
                    if str(status).__contains__('jr'):
                        print ("=> end with jr")
                        break
                    if str(status).__contains__("262010"):
                        self.transactionRequest(price, date, is_preauth)
                    
                    self.__uart.write(bytes(b"\x06"))
                status = ""

    def readStatusPreAuth(self):
        self.__status_list = []
        is_start= False	
        status = ""
        while not self.__is_stop:
            response = self.__uart.read()
            response = self.byteString2String(response)
            if response == "06":
                print ("0x06")
            if response == "02":
                is_start = True
                continue
            elif response == "03": 
                is_start = False	
                continue
            
            if is_start:
                status += response
            else:                    
                if status != "":            
                    self.setStatus(status)
                    code = str(status)[2:6]
                    result = breakStatus(code)
                    if str(status).__contains__('5F'):
                        print ("=> end with 5F")
                        self.__uart.write(bytes(b"\x06"))
                        break
                    if result != ("Invalid status"):
                        print ("=> " + result)
                        break
                    self.__uart.write(bytes(b"\x06"))
                status = ""

    def transactionRequest(self, price, date, is_preauth):
        """ Transaction Request (Ex2)

            Attributes:
                price: xx...xx,xx
                date: dd-mm-yy
                is_preauth: True/False
                    True: Transaction type -> Initial Preauthorization
                    False: Transaction type -> Normal Purchase
            Return:
                String hex format
        """

        try:
            price_list = self.convertPriceToList(price)

            date_hex = []
            for i in range(0,len(date)):
                if date[i] != "-":
                    date_hex.append(date[i].encode("utf-8").hex())

            command = bytearray(83)
            command[0] = STX
            command[1] = 0x79                           # y - messageID
            
            if is_preauth:
                command[2] = 0x50                           # P = Initial Preauthorization
            else:
                command[2] = 0x30                           # 0 - Transaction type - purchase

            command[3] = int(price_list[0],16)             # Amount 12 bytes
            command[4] = int(price_list[1],16)             # Amount
            command[5] = int(price_list[2],16)             # Amount
            command[6] = int(price_list[3],16)             # Amount
            command[7] = int(price_list[4],16)             # Amount
            command[8] = int(price_list[5],16)             # Amount
            command[9] = int(price_list[6],16)             # Amount
            command[10] = int(price_list[7],16)            # Amount
            command[11] = int(price_list[8],16)            # Amount
            command[12] = int(price_list[9],16)            # Amount
            command[13] = int(price_list[10],16)           # Amount
            command[14] = int(price_list[11],16)           # Amount
            command[15] = 0x30      # Cashback 12 bytes
            command[16] = 0x30      # Cashback
            command[17] = 0x30      # CashbackconvertPriceToList
            command[18] = 0x30      # CashbackconvertPriceToList
            command[19] = 0x30      # CashbackconvertPriceToList
            command[20] = 0x30      # CashbackconvertPriceToList
            command[21] = 0x30      # Cashback
            command[22] = 0x30      # Cashback
            command[23] = 0x30      # Cashback
            command[24] = 0x30      # Cashback
            command[25] = 0x30      # Cashback
            command[26] = 0x30      # Cashback
            command[27] = 0x30      # TransactionID 5 bytes
            command[28] = 0x30      # TransactionID 
            command[29] = 0x30      # TransactionID 
            command[30] = 0x30      # TransactionID 
            command[31] = 0x30      # TransactionID 
            command[32] = 0x31      # Force Authorization 
            command[33] = 0x30      # Manual card number
            command[34] = 0x30      # Bonus handled
            command[35] = 0x1c      # 1c - Authoriztion code
            command[36] = 0x30      # Authoriztion code
            command[37] = 0x30      # Authoriztion code
            command[38] = 0x30      # Authoriztion code
            command[39] = 0x30      # Authoriztion code
            command[40] = 0x30      # Authoriztion code
            command[41] = 0x30      # Authoriztion code
            command[42] = 0x30      # Timestamp 12 bytes
            command[43] = 0x30      # Timestamp
            command[44] = 0x30      # Timestamp
            command[45] = 0x30      # Timestamp
            command[46] = 0x30      # Timestamp
            command[47] = 0x30      # Timestamp
            command[48] = 0x30      # Timestamp
            command[49] = 0x30      # Timestamp
            command[50] = 0x30      # Timestamp
            command[51] = 0x30      # Timestamp
            command[52] = 0x30      # Timestamp
            command[53] = 0x30      # Timestamp
            command[54] = 0x30      # Serial No 9 bytes
            command[55] = 0x30      # Serial No
            command[56] = 0x30      # Serial No
            command[57] = 0x30      # Serial No
            command[58] = 0x30      # Serial No
            command[59] = 0x30      # Serial No
            command[60] = 0x30      # Serial No
            command[61] = 0x30      # Serial No
            command[62] = 0x30      # Serial No
            command[63] = 0x46      # Payment method restriction
            command[64] = 0x30      # Surcharge handled
            command[65] = 0x31      # LookForDOB
            command[66] = 0x30      # Flags
            command[67] = 0x30      # Whitelist
            command[68] = 0x39      # Currency 3 bytes
            command[69] = 0x37      # Currency
            command[70] = 0x38      # Currency
            command[71] = int(date_hex[0],16)      # Accounting date 6 bytes
            command[72] = int(date_hex[1],16)      # Accounting date 
            command[73] = int(date_hex[2],16)      # Accounting date 
            command[74] = int(date_hex[3],16)      # Accounting date 
            command[75] = int(date_hex[4],16)      # Accounting date 
            command[76] = int(date_hex[5],16)      # Accounting date 
            command[77] = 0x30      # Accounting date sequence
            command[78] = 0x30      # RFU
            command[79] = 0x33      # ECR number 2 bytes
            command[80] = 0x38      # ECR number
            command[81] = ETX
            command[82] = self.calculateLCR(command)
		
            print (self.byteString2String(command))

            self.__uart.write(command)

            #response = self.__uart.read()
            #if binascii.hexlify(response) == "06":
            #    print binascii.hexlify(response)
            #    return True
            #return False

            return True
        except Exception as e:
            print (e)

    def preauthorizedTransactionRequest(self, price, preauthorized_id):
        """ Preauthorized Transaction Request

            Attributes:
                price: xx...xx,xx ; total amount 
                preauthorized_id: String
            Return:
                String hex format
        """
        try:
            price_list = self.convertPriceToList(price)

            preauth_id = []
            for i in range(0,22):
                if i >= len(preauthorized_id):
                    preauth_id.insert(0,' '.encode("utf-8").hex())
                else:
                    preauth_id.append(preauthorized_id[i].encode("utf-8").hex())

            command = bytearray(51)
            command[0] = STX
            command[1] = 0x30                              # 0 - messageID
            command[2] = int(price_list[0],16)             # Amount 12 bytes
            command[3] = int(price_list[1],16)             # Amount
            command[4] = int(price_list[2],16)             # Amount
            command[5] = int(price_list[3],16)             # Amount
            command[6] = int(price_list[4],16)             # Amount
            command[7] = int(price_list[5],16)             # Amount
            command[8] = int(price_list[6],16)             # Amount
            command[9] = int(price_list[7],16)             # Amount
            command[10] = int(price_list[8],16)            # Amount
            command[11] = int(price_list[9],16)            # Amount
            command[12] = int(price_list[10],16)           # Amount
            command[13] = int(price_list[11],16)           # Amount
            
            if price == "0" or price == "0.00":
                command[14] = 0x33                             # Type '3' = Cancel transaction
            else:
                command[14] = 0x31                             # Type '1' = Finalize transaction
            
            command[15] = int(preauth_id[0],16)     # preauthorized ID 22 bytes
            command[16] = int(preauth_id[1],16)      # preauthorized ID
            command[17] = int(preauth_id[2],16)      # preauthorized ID
            command[18] = int(preauth_id[3],16)      # preauthorized ID
            command[19] = int(preauth_id[4],16)      # preauthorized ID
            command[20] = int(preauth_id[5],16)      # preauthorized ID
            command[21] = int(preauth_id[6],16)      # preauthorized ID
            command[22] = int(preauth_id[7],16)      # preauthorized ID
            command[23] = int(preauth_id[8],16)      # preauthorized ID
            command[24] = int(preauth_id[9],16)      # preauthorized ID
            command[25] = int(preauth_id[10],16)      # preauthorized ID
            command[26] = int(preauth_id[11],16)      # preauthorized ID
            command[27] = int(preauth_id[12],16)      # preauthorized ID 
            command[28] = int(preauth_id[13],16)      # preauthorized ID 
            command[29] = int(preauth_id[14],16)      # preauthorized ID 
            command[30] = int(preauth_id[15],16)      # preauthorized ID 
            command[31] = int(preauth_id[16],16)      # preauthorized ID 
            command[32] = int(preauth_id[17],16)      # preauthorized ID
            command[33] = int(preauth_id[18],16)      # preauthorized ID
            command[34] = int(preauth_id[19],16)      # preauthorized ID
            command[35] = int(preauth_id[20],16)      # preauthorized ID
            command[36] = int(preauth_id[21],16)      # preauthorized ID
            command[37] = 0x30      # RFU 12 bytes
            command[38] = 0x30      # RFU
            command[39] = 0x30      # RFU
            command[40] = 0x30      # RFU
            command[41] = 0x30      # RFU
            command[42] = 0x30      # RFU
            command[43] = 0x30      # RFU
            command[44] = 0x30      # RFU
            command[45] = 0x30      # RFU
            command[46] = 0x30      # RFU
            command[47] = 0x30      # RFU
            command[48] = 0x30      # RFU
            command[49] = ETX
            command[50] = self.calculateLCR(command)

            print (self.byteString2String(command))
            self.__uart.write(command)	
            #if binascii.hexlify(response) == "06":
            #    print binascii.hexlify(response)
            #    return True
            #return False
            return True
        except Exception as e:
            print (e)

    def convertHexFormat(self, string):
        string_temp = ""
        for i in range(0,len(string),2):
            string_temp += "\\x" + string[i:i+2]
        return string_temp

    def convertPriceToList(self, price):
        if "." in price:
            if len(price) == price.index(".") + 2:
                price += "0"
        else:
            price += ".00"

        price = price.replace(".","")
        price_list = []
        for i in range(0,12):
            if i >= len(price):
                price_list.insert(0, '0'.encode("utf-8").hex())
            else:
                price_list.append(price[i].encode("utf-8").hex())
        return price_list

    def createTransaction(self, price, is_preauth):
        """ Create transaction

            Attributes:
                price: xx...xx,xx ; amount 
                is_preauth: True/False
                    True: Initial Preauthorization
                    False: Normal Purchase
        """
        while not self.__is_stop and self.isOpen(): 
            if self.writeENQ():
                break
            time.sleep(1)

        while not self.__is_stop and self.isOpen():
            if self.transactionRequest(price=price, date=self.currentDate(), is_preauth=is_preauth):
                break
            time.sleep(1)
        self.readStatus(price=price, date=self.currentDate(), is_preauth=is_preauth)
    
    def createPreauthorizedTransaction(self, price, preauth_id):
        """ Create preauthorized transaction

            Attributes:
                price: xx...xx,xx ; amount 
                preauth_id: preauthorizationID
        """
        while not self.__is_stop:
            if self.writeENQ():
                break
            time.sleep(1)

        while not self.__is_stop:
            if self.preauthorizedTransactionRequest(price=price, preauthorized_id=preauth_id):
                break
            time.sleep(1)

        self.readStatusPreAuth()

    def setStatus(self, status):
        status = str(status)
        print (status)
        self.__status_list.append(status)
        self.updateStatus(status)
        return status

    def getStatusList(self):
        return self.__status_list

    def getPreauthID(self):
        """ Get PreauthorizationID
        """  
        for status in self.getStatusList():
            if status[0:6] == "2#0000":
                return status[6:28]

    def currentDate(self):
        """ Get current date following dd-mm-yy format
        """
        date = str(datetime.now())
        return date[8:10] + "-" + date[5:7] + "-" + date[2:4]
    
    def close(self):
        self.__uart.close()

    def setStop(self, is_stop):
        self.__is_stop = is_stop

    def byteString2String(self, data):
        try:
            return binascii.hexlify(data).decode("utf-8")
        except Exception:
            return '' 