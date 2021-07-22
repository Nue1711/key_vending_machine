class RemoteControl:
    PROJECT_ID = 'autoklinikka-267610'
    REQUEST_FROM_WEB_TOPIC = '{}/{}'.format(PROJECT_ID, 'requestFromWeb')
    RESPONSE_FROM_MACHINE_TOPIC = '{}/{}'.format(PROJECT_ID, 'responseFromMachine')
    SOCKET_URL = 'http://35.228.160.75:65080'
    LOCAL_SOCKET_URL = 'http://localhost:65080'

class RCMessageType:
    REQ = 101
    RSP = 102

class RCDoorPosition:
    ABOVE = 301
    BELOW = 302

class RCRequestCode:
    TOGGLE_DOOR = 131
    RELEASE_KEY = 132

class RCResponseCode:
    OK = 200
    OPERATION_NOT_SUPPORTED = 230
    INVALID_PARAMETER = 231
    INVALID_OPERATION = 232
    PROTOCOL_VERSION_NOT_SUPPORTED = 233
    FAIL = 234
    TIMEOUT = 250
    BUSY = 256




