from utils.write_log import writeExceptionToFile

def checkEnableBitKey(dict_dt, key_number):
    """ Check enable bit postition in response key 

        Note: Count from right to left of bit string
    """
    data = dict_dt["data"]
    if len(data) < 4:
        return False
    if key_number % 10 == 0:
        slave_number = (key_number / 10)
        key_pos = 9
    else:
        slave_number = (key_number / 10) + 1
        key_pos = (key_number % 10) - 1
    data_bin = ""

    try:
        for x in data:
            data_bin += bin(int(x, 16))[2:].zfill(4)
    except ValueError :
        return False

    s1 = data_bin[::-1]
    data_bin = ''.join(s1)
    if slave_number == int(dict_dt["slave"]):
        if data_bin[key_pos] == '1':
            return True
        else:
            return False
    return False

def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def checkEnableBitDoor(hex_string, bit):
    """ Check enable bit postition in response door 

        Note: Count from right to left of bit string
    """
    try:
        data = hex_string[8:12].decode('utf-8')
        data_bin = ''
        try:
            for x in data:
                x = str(x)
                data_bin += bin(int(x, 16))[2:].zfill(4)
        except ValueError as e:
            return False
        s1 = data_bin[::-1]
        data_bin = ''.join(s1)
        if data_bin[bit] == '1':
            return True
        return False
    except Exception as e:
        print(e)
        writeExceptionToFile()
        return False

# is_open_door = False
# response = b'f70302080c1008'
# a = (is_open_door and not checkEnableBitDoor(response, 11)) or (not is_open_door and checkEnableBitDoor(response, 11))
# print(a)