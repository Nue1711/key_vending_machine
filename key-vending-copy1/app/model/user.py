from PyQt5.QtCore import QObject, pyqtSignal

class User(QObject):
    
    name_changed = pyqtSignal(str)
    customer_status_changed = pyqtSignal(str)
    door_status_changed = pyqtSignal(str)
    vehicle_changed = pyqtSignal(str)
    reserved_time_changed = pyqtSignal(int)
    balance_changed = pyqtSignal(float)
    qr_code_changed = pyqtSignal(bool)
    receipt_changed = pyqtSignal(str)
    status_changed = pyqtSignal(str)
    booking_id_changed = pyqtSignal(str)
    key_position_changed = pyqtSignal(int)
    repair_costs_changed = pyqtSignal(int)
    damage_description_changed = pyqtSignal(str)
    serial_machine_changed =pyqtSignal(int)
    user_id_changed = pyqtSignal(str)
    check_in_date_changed = pyqtSignal(int)
    repair_note_changed = pyqtSignal(str)
    assign_date_changed =pyqtSignal(str)
    phone_number_changed = pyqtSignal(str)
    bill_changed = pyqtSignal(str)
    check_out_date_changed = pyqtSignal(str)
    return_date_changed = pyqtSignal(str)
    pay_bill_date_changed = pyqtSignal(str)
    done_date_changed = pyqtSignal(str)
    index_changed = pyqtSignal(int)
    machine_name_changed=pyqtSignal(str)
    booking_date_changed=pyqtSignal(int)
    checked_in_date_changed =pyqtSignal(str)
    plate_number_changed = pyqtSignal(str)
    id_changed = pyqtSignal(int)
    input_number_changed = pyqtSignal(int)
    frame_changed = pyqtSignal(int)


    def __init__(self):
        super().__init__()
        self.__name = ''
        self.__customer_status = ''
        self.__door_status = ''
        self.__vehicle = ''
        self.__reserved_time = ''
        self.__balance = ''
        self.__qr_code = ''
        self.__receipt = ''
        self.__status = ''
        self.__booking_id = ''
        self.__key_position = ''
        self.__repair_costs = ''
        self.__damage_description =''
        self.__serial_machine =''
        self.__user_id = ''
        self.__check_in_date =''
        self.__repair_note =''
        self.__assign_date = ''
        self.__phone_number = ''
        self.__bill = ''
        self.__check_out_date = ''
        self.__return_date = ''
        self.__pay_bill_date = ''
        self.__done_date = ''
        self.__index = ''
        self.__machine_name = ''
        self.__booking_date = ''
        self.__checked_in_date = ''
        self.__plate_number = ''
        self.__id = ''
        self.__input_number =''
        self.__frame =''



    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        self.name_changed.emit(value)

    @property
    def customer_status(self):
        return self.__customer_status

    @customer_status.setter
    def customer_status(self, value):
        self.__customer_status = value
        self.customer_status_changed.emit(value)
    
    @property
    def door_status(self):
        return self.__door_status

    @door_status.setter
    def door_status(self, value):
        self.__door_status = value
        self.door_status_changed.emit(value)

    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self, value):
        self.__name = value
        self.frame_changed.emit(value)    

    @property
    def vehicle(self):
        return self.__vehicle

    @vehicle.setter
    def vehicle(self, value):
        self.__vehicle = value
        self.vehicle_changed.emit(value)

    @property
    def reserved_time(self):
        return self.__reserved_time

    @reserved_time.setter
    def reserved_time(self, value):
        self.__reserved_time = value
        self.reserved_time_changed.emit(value)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value
        self.balance_changed.emit(value)

    @property
    def qr_code(self):
        return self.__qr_code

    @qr_code.setter
    def qr_code(self, value):
        self.__qr_code = value
        self.qr_code_changed.emit(value)

    @property
    def receipt(self):
        return self.__receipt

    @receipt.setter
    def receipt(self, value):
        self.__receipt = value
        self.receipt_changed.emit(value)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
        self.status_changed.emit(value)

    @property
    def booking_id(self):
        return self.__booking_id

    @booking_id.setter
    def booking_id(self, value):
        self.__booking_id = value
        self.booking_id_changed.emit(value)

    @property
    def key_position(self):
        return self.__key_position

    @key_position.setter
    def key_position(self, value):
        self.__key_position = value
        self.key_position_changed.emit(value)

    @property
    def repair_costs(self):
        return self.__repair_costs

    @repair_costs.setter
    def repair_costs(self, value):
        self.__repair_costs = value
        self.repair_costs_changed.emit(value)   

    @property
    def damage_description(self):
        return self.__damage_description

    @damage_description.setter
    def damage_description(self, value):
        self.__damage_description = value
        self.damage_description_changed.emit(value) 

    @property
    def serial_machine(self):
        return self.__serial_machine

    @serial_machine.setter
    def serial_machine(self, value):
        self.__serial_machine = value
        self.serial_machine_changed.emit(value)  

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value
        self.user_id_changed.emit(value)

    @property
    def check_in_date(self):
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        self.__check_in_date = value
        self.check_in_date_changed.emit(value)

    @property
    def repair_note(self):
        return self.__repair_note

    @repair_note.setter
    def repair_note(self, value):
        self.__repair_note = value
        self.repair_note_changed.emit(value)   

    @property
    def assign_date(self):
        return self.__assign_date

    @assign_date.setter
    def assign_date(self, value):
        self.__assign_date = value
        self.assign_date_changed.emit(value)   

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value
        self.phone_number_changed.emit(value)  

    @property
    def bill(self):
        return self.__bill

    @bill.setter
    def bill(self, value):
        self.__bill = value
        self.bill_changed.emit(value)    

    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, value):
        self.__check_out_date = value
        self.check_out_date_changed.emit(value)

    @property
    def return_date(self):
        return self.__return_date

    @return_date.setter
    def return_date(self, value):
        self.__return_date = value
        self.return_date_changed.emit(value)

    @property
    def pay_bill_date(self):
        return self.__pay_bill_date

    @pay_bill_date.setter
    def pay_bill_date(self, value):
        self.__pay_bill_date = value
        self.pay_bill_date_changed.emit(value) 
    
    @property
    def _done_date(self):
        return self.___done_date

    @_done_date.setter
    def _done_date(self, value):
        self.___done_date = value
        self._done_date_changed.emit(value)
    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, value):
        self.__index = value
        self.index_changed.emit(value)

    @property
    def machine_name(self):
        return self.__machine_name

    @machine_name.setter
    def machine_name(self, value):
        self.__machine_name = value
        self.machine_name_changed.emit(value)

    @property
    def booking_date (self):
        return self.__booking_date 

    @booking_date .setter
    def booking_date (self, value):
        self.__booking_date  = value
        self.booking_date_changed.emit(value)

    @property
    def checked_in_date(self):
        return self.__checked_in_date

    @checked_in_date.setter
    def checked_in_date(self, value):
        self.__checked_in_date = value
        self.checked_in_date_changed.emit(value)
    
    @property
    def plate_number(self):
        return self.__plate_number

    @plate_number.setter
    def plate_number(self, value):
        self.__plate_number = value
        self.plate_number_changed.emit(value)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
        self.id_changed.emit(value)

    @property
    def input_number(self):
        return self.__input_number

    @input_number.setter
    def input_number(self, value):
        self.__input_number = value
        self.input_number_changed.emit(value)
'''
def gett(name):
    print ("@property\ndef " + name[2:] + "(self):\n    return self." + name + "\n")
    print ("@"+name[2:]+".setter\ndef " + name[2:] + "(self, value):\n    self." + name + " = value")
    print ("    self." +name[2:]+"_changed.emit(value)")
gett("__id")
'''

