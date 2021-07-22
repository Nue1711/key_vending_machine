from PyQt5.QtCore import QThread, pyqtSignal
from constant.device_port import DevicePort
from utils.write_log import writeExceptionToFile, writeExecutionSteps
from utils.find_serial_port import FindSerialPort
from utils.observable_trigger import ObservableTrigger
from key_and_door.controller_key_door import ControllerKeyDoor
from key_and_door.check_key_and_door_status import checkEnableBitDoor
obs = ObservableTrigger.getInstance()

class ThreadControlDoor(QThread):
    """ Thread control door

        Attributes:
            command: 'dropKey', 'takeKey', 'closeAllDoor'
            request_result: result post
    """

    control_result = pyqtSignal(bool)

    def __init__(self, command, key_number=None):
        QThread.__init__(self)
        self.__command = command
        self.__key_number = key_number
        self.__initController()

    def __initController(self):
        port = FindSerialPort()
        port_name = port.getDeviceByHardwareID(DevicePort.KEY_DOOR)
        if port_name == None:
                obs.trigger("hardwareError")
                return
        self.__controller_key_door = ControllerKeyDoor(port_name)

    def run(self):
        try:
            if not self.__controller_key_door.initialize():
                return
                
            if (self.__command == 'dropKey'):
                self.dropKey()
            elif (self.__command == 'takeKey'):
                self.takeKey()
            elif (self.__command == 'closeAllDoor'):
                self.closeAllDoor()

        except Exception as e:
            writeExceptionToFile()
            self.control_result.emit(False)
        finally:
            # self.__controller_key_door.close()
            pass

    def dropKey(self):
        result =  self.__controller_key_door.dropKey()
        self.control_result.emit(result)

    def takeKey(self):
        result = self.__controller_key_door.takeKey(self.__key_number)
        self.control_result.emit(result)

    def closeAllDoor(self):
        count = 0
        __is_take_door_closed = False
        __is_return_door_closed = False

        while True:
            try:
                if (count == 3):
                    self.control_result.emit(False)
                    return False
                    
                if checkEnableBitDoor(self.__controller_key_door.getDoorStatus(is_return_door=False), 11):
                    __is_take_door_closed = self.__controller_key_door.toggleDoor(is_return_door=False)
                else:
                    __is_take_door_closed = True
                
                if checkEnableBitDoor(self.__controller_key_door.getDoorStatus(is_return_door=True), 11):
                    __is_return_door_closed = self.__controller_key_door.toggleDoor(is_return_door=True)
                else:
                    __is_return_door_closed = True

                if __is_take_door_closed and __is_return_door_closed:
                    writeExecutionSteps('All door are closed')
                    self.control_result.emit(True)
                    break
            except Exception:
                writeExceptionToFile()
                continue
            finally:
                count += 1

    def closeControlDoor(self):
        self.__controller_key_door.close()