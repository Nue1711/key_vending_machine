import serial
import binascii
from key_and_door.check_key_and_door_status import checkEnableBitDoor, checkEnableBitKey 
from utils.write_log import writeExecutionSteps, writeExceptionToFile
import time
from utils.observable_trigger import ObservableTrigger
obs = ObservableTrigger.getInstance()

CTRL_BYTE = 0xF7
GO_CMD = 0x04
POLL_CMD = 0x02
RESET_CMD = 0x01

class ControllerKeyDoor:
    """ Controller key
        
        Control open key
        
        Attributes:
            com_port: port device
            chk_byte: 0 or 1, invert the bit every time the request to firmware
            uart: communication with firmware 
    """
    def __init__(self, com_port=None):
        self.com_port = com_port
        self.__chk_byte = 0x00
        self.__uart = None

    def initialize(self):
        try:
            self.__uart = serial.Serial()  # BR 9600, 8, N, 1
            self.__uart.port = self.com_port
            self.__uart.timeout = 3
            self.__uart.open()
            if self.__uart.isOpen():
                return True
            else:
                obs.trigger("hardwareError")
                return False
        except serial.serialutil.SerialException as error:
            writeExceptionToFile()
            obs.trigger("hardwareError")
            return False

    def isOpen(self):
        if not self.__uart.isOpen():
            obs.trigger("hardwareError")
        return self.__uart.isOpen()

    def close(self):
        self.__uart.close()

    def __createCommand(self, pos0, pos1, pos2, pos4, pos6):
        command = bytearray(8)
        try:
            command[0] = pos0
            command[1] = pos1
            command[2] = pos2
            command[3] = 0x02  # DATA size
            command[4] = pos4
            command[5] = 0x00
            command[6] = pos6

            # checksum
            command[7] = self.__calculateChecksum(command)
            return command
        except Exception as e:
            print(e)
            return command

    @staticmethod
    def __calculateChecksum(byte_array):
        checksum = 0x00
        for b in byte_array:
            checksum += b
        return checksum & 0xFF

    def releaseKey(self, key_number):
        print ("Open key: " + str(key_number))
        # writeExecutionSteps("Open key: " + str(key_number))
        if key_number not in range(1, 51):
            print ('invalid key number')
            return False

        if key_number % 10 == 0:
            slave_number = (key_number // 10)
            key_pos = 9
        else:
            slave_number = (key_number // 10) + 1
            key_pos = (key_number % 10) - 1

        command = self.__createCommand(CTRL_BYTE, self.__chk_byte, slave_number, GO_CMD, key_pos)
        # print(binascii.hexlify(command))        
        response = self.__writeCommand(command)
        if response:
            print (self.__binascii2String(response))
            writeExecutionSteps("Response open key " + str(key_number) + " : " + self.__binascii2String(response))
            self.__chk_byte ^= 0x01
            return True
        return False

    def toggleReturnDoor(self, is_open_door):
        door_status = self.getDoorStatus(is_return_door=True)
        print ('toggleReturnDoor status ' + str(is_open_door) + str(door_status))

        if door_status != '':
            if ((is_open_door and not checkEnableBitDoor(door_status,11)) or
                (not is_open_door and checkEnableBitDoor(door_status,11))):                
                
                command = self.__createCommand(CTRL_BYTE, self.__chk_byte, 0x03, GO_CMD, 0x0B)

                response = self.__writeCommand(command)
                if response:
                    print (self.__binascii2String(response))
                    writeExecutionSteps("Response open/close return door: " + self.__binascii2String(response))
                    self.__chk_byte ^= 0x01
                    return True

                return False
            else:
                writeExecutionSteps("Return door is opened/closed: ")
                return True
        else:
            return False
    
    def toggleTakeDoor(self, is_open_door):
        door_status = self.getDoorStatus(is_return_door=False)
        print ('toggleTakeDoor status ' + str(is_open_door) + str(door_status))
        if door_status != '':
            if ((is_open_door and not checkEnableBitDoor(door_status,11)) or
                (not is_open_door and checkEnableBitDoor(door_status,11))):                
                
                command = self.__createCommand(CTRL_BYTE, self.__chk_byte, 0x04, GO_CMD, 0x0B)

                response = self.__writeCommand(command)
                if response:
                    print (self.__binascii2String(response))
                    writeExecutionSteps("Response open/close take door: " + self.__binascii2String(response))
                    self.__chk_byte ^= 0x01
                    return True
                return False
            else:
                writeExecutionSteps("Take door is opened/closed: ")
                return True
        else:
            return False
    
    def toggleDoor(self, is_return_door):
        if is_return_door:
            command = self.__createCommand(CTRL_BYTE, self.__chk_byte, 0x03, GO_CMD, 0x0B)
        else:
            command = self.__createCommand(CTRL_BYTE, self.__chk_byte, 0x04, GO_CMD, 0x0B)
        response = self.__writeCommand(command)
        if response:
            print (self.__binascii2String(response))
            writeExecutionSteps("Response open/close take door: " + self.__binascii2String(response))
            self.__chk_byte ^= 0x01
            return True
        return False

    def dropKeyToBox(self):
        command = self.__createCommand(CTRL_BYTE, self.__chk_byte, 0x05, GO_CMD, 0x0B)
        response = self.__writeCommand(command)
        if response:
            print (self.__binascii2String(response))
            writeExecutionSteps("Drop key to box")
            self.__chk_byte ^= 0x01
            return True
        return False

    def dropKeyToBoxRC(self):
        count = 1
        while not self.dropKeyToBox():
            time.sleep(0.5)
            self.__chk_byte ^= 0x01
            count += 1
            if count == 3:
                return False
        return True

    def toggleTakeDoorRC(self, is_open_door):
        count = 1
        while not self.toggleTakeDoor(is_open_door):
            time.sleep(0.5)
            self.__chk_byte ^= 0x01
            count += 1
            if count == 3:
                return False
        return True

    def toggleReturnDoorRC(self, is_open_door):
        count = 1
        while not self.toggleReturnDoor(is_open_door):
            time.sleep(0.5)
            self.__chk_byte ^= 0x01
            count += 1
            if count == 3:
                return False
        return True
    
    def releaseKeyRC(self, key_number):
        count = 1
        while not self.releaseKey(key_number):
            time.sleep(0.5)
            self.__chk_byte ^= 0x01
            count += 1
            if count == 3:
                return False
        return True

    def __reset(self):
        command = self.__createCommand(CTRL_BYTE, self.__chk_byte, 0x05, RESET_CMD, 0x0B)
        response = self.__writeCommand(command)
        if response:
            self.__chk_byte ^= 0x01
            print (self.__binascii2String(response))
            writeExecutionSteps("Reset: " + self.__binascii2String(response))
            return True
        return False

    def resetFirmware(self):
        while not self.__reset():
            time.sleep(1)
            self.__chk_byte ^= 0x01

    def takeKey(self, key_number):
        count = 1
        count_reset = 1
        if self.isOpen():
            # release key
            while not self.releaseKey(int(key_number)):
                time.sleep(1)
                self.__chk_byte ^= 0x01
                count += 1
                if count == 10:
                    if count_reset == 3:
                        return False
                    self.resetFirmware()
                    count = 1
                    count_reset += 1
            count = 1
            count_reset = 1
            time.sleep(1)

            # open take key door
            while not self.toggleTakeDoor(is_open_door=True):
                time.sleep(1)
                self.__chk_byte ^= 0x01
                count += 1
                if count == 10:
                    if count_reset == 3:
                        return False
                    self.resetFirmware()
                    count = 1
                    count_reset += 1
            count = 1
            count_reset = 1

            obs.trigger("closeDoor")

            time.sleep(15)

            # close take key door
            while not self.toggleTakeDoor(is_open_door=False):
                time.sleep(1)
                self.__chk_byte ^= 0x01
                count += 1
                if count == 10:
                    if count_reset == 3:
                        return False
                    self.resetFirmware()
                    count = 1
                    count_reset += 1
            count = 1
            count_reset = 1

            return True
        else:
            return False

    def dropKey(self):
        count = 1
        count_reset = 1
        if self.isOpen():
            # open return door
            while not self.toggleReturnDoor(is_open_door=True):
                time.sleep(1)
                self.__chk_byte ^= 0x01
                count += 1
                if count == 10:
                    if count_reset == 3:
                        return False
                    self.resetFirmware()
                    count = 1
                    count_reset += 1
            count = 1
            count_reset = 1
            
            obs.trigger("closeDoor")
            
            time.sleep(15)
            
            # close return door
            while not self.toggleReturnDoor(is_open_door=False):
                time.sleep(1)
                self.__chk_byte ^= 0x01
                count += 1
                if count == 10:
                    if count_reset == 3:
                        return False
                    self.resetFirmware()
                    count = 1
                    count_reset += 1
            count = 1
            count_reset = 1
            time.sleep(2)

            # drop key to box
            while not self.dropKeyToBox():
                time.sleep(1)
                self.__chk_byte ^= 0x01
                count += 1
                if count == 10:
                    if count_reset == 3:
                        return False
                    self.resetFirmware()
                    count = 1
                    count_reset += 1
            count = 1
            count_reset = 1

            return True
        else:
            return False

    def getDoorStatus(self, is_return_door):
        count = 0
        if self.isOpen():
            while (count < 5):
                time.sleep(1)
                if is_return_door:
                    command = self.__createCommand(CTRL_BYTE, self.__chk_byte, 0x03, POLL_CMD, 0x0B)
                else:
                    command = self.__createCommand(CTRL_BYTE, self.__chk_byte, 0x04, POLL_CMD, 0x0B)
                response = self.__writeCommand(command)
                if response:
                    self.__chk_byte ^= 0x01
                    return binascii.hexlify(response)
                else:
                    self.__chk_byte ^= 0x01
                count += 1
        else:
            return ''
        return ''

    def __writeCommand(self, command):
        try:
            self.__uart.write(command)
            # read back response
            return self.__uart.read(8)
        except Exception as e:
            print(e)
            writeExceptionToFile()
            return False
        finally:
            pass

    def __binascii2String(self, bin_data):
        try:
            return str(binascii.hexlify(bin_data))
        except Exception as e:
            return ''
