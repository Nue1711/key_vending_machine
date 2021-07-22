import sys
import glob
import serial

class FindSerialPort():
    def __init__(self):
        super().__init__()
        pass

    def serialPorts(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/ttys*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    def getDeviceByHardwareID(self, vpid):
        """ Lists serial port by vendor ID and product ID
            
            vpid: <vendorID>:<productID>

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        from serial.tools.list_ports import comports
        devs = comports()
        for dev in devs:
            port, desc, hwid = dev
                        
            if hwid == None:
                continue
            try:
                vpid_temp = hwid.split(' ')
                vpid_temp = vpid_temp[1].split('=')
                if vpid_temp[1].lower() == vpid.lower():
                    return port
            except Exception as e:
                continue           
        return None