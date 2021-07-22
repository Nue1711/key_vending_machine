from constant.language import Language

class DefaultString():    
    @staticmethod
    def getDefaultString():
        language = Language.getLanguage()
        if language == Language.EN:
            return DefaultStringEN()
        
        if language == Language.FI:
            return DefaultStringFI()

class DefaultStringEN():
    WELCOME = 'Welcome!'
    PLEASE_SHOW_QR = 'Please show QR-code to reader'
    PLEASE_SHOW_QR_INFO = 'Set brightness to max at your phone and show QR-code to reader'
    PLEASE_WAIT = 'Please wait...'
    LOOKING_FOR_CODE = 'Looking for code'
    HELLO = 'Hello!'
    HAVE_A_NICE_DAY =' have a nice day'
    NAME = 'Name'
    YOUR_VEHICLE = 'Your vehicle plate number: '
    YOUR_PHONE_NUMBER = 'Your phone number: '
    RESERVED_TIME = 'Reserved service time is'
    QR_NOT_FOUND = 'QR-code not found'
    PLEASE_WAIR_SUB_KEY ='Please wait for substitute vehicle key'
    PLEASE_DROP_SUB_KEY = 'Please drop the substitute key'
    
    TAKE_PIC = "Take Picture"
    SIGN_IN = 'Sign In'
    SIGNUP = 'Sign Up'
    LOGIN = 'LOGIN HERE'
    SIGN_UP = 'OFFICIAL SIGNUP FORM' 
    
    TRAINING_FACE = 'TRAINING FACE CAMERA'
    WAIT = 'PLEASE WAIT IN A FEW MINUTES'

    
    PLEASE_CALL_SERVICE = 'Please call service number 020 773 7437'
    PLEASE_CALL_CUSTOMER_SERVICE ='Please call customer service 09-123456'

    PLEASE_DROP_KEY = 'Please drop your own car key to the Locker'
    REG_PLATE = 'The vehicle reg plate is '
    SUB_CAR ='You have substitute vehicle'

    SHUT_DOOR_AFTER_THREE_DOT = ''
    SHUT_DOOR_AFTER = ''
    SHUT_DOOR = ''
    THANK_YOU_INFORM = 'Thank you, We \ninform when vehicle \nis ready to pickup'
    THANK_YOU = 'Thank You,'
    OPEN_BALANCE = 'Open balance is '
    PAY = 'Pay'
    NEXT = 'Next'
    PLEASE_FOLLOW_INSTRUCTION_PAYMENT = 'Please follow instructions on the payment device!'
    PLEASE = 'Please..'
    FULL = "This machine is full now, please try another one!\n We're sorry for the inconvenience"
    TAKE_KEY_THREE_DOT = '...take the key from the closet'
    TAKE_KEY = 'Take the key from the locker'
    PAYMENT_OK = 'Payment OK'
    PAYMENT_FAILED =  'Payment Failed!'
    PICK_UP_KEY = ' Pick up your own key'
    FOR_USING =  'For using Autoklinikka'
    NOT_CONNECT_INTERNET =  'Not connected to internet'
    NO_CAMERA = 'We can not find your camera'
    TRY_AGAIN =  'Please try again!'
    HARDWARE_ERROR =  'Hardware error'
    DOOR_WILL_CLOSE =  'The door will close after'
    DOOR_OPENING =  'Please wait'
    SECOND =  'second'
    SECONDS =  'seconds'
    START =  'Start'

class DefaultStringFI():
    WELCOME = 'Avainautomaatti'
    PLEASE_SHOW_QR = 'Näytä QR-koodi lukijalle'
    PLEASE_SHOW_QR_INFO = 'Säädä puhelimen näyttö kirkkaaksi ja näytä QR-koodi lukijalle.'
    PLEASE_WAIT = 'Pieni hetki..'
    LOOKING_FOR_CODE = 'QR-koodiasi luetaan parhaillaan'
    HELLO = 'Tiedot'
    HAVE_A_NICE_DAY =' hauskaa päivän jatkoa'
    NAME = 'Nimi'
    YOUR_VEHICLE = 'Auton rekisterinumero'
    RESERVED_TIME = 'Autollesi varattu korjausaika'
    QR_NOT_FOUND = 'Antamaasi QR-koodia ei löytynyt'
    PLEASE_CALL_SERVICE = 'Yritä uudelleen tai soita\n24h palvelunumeroomme 020 773 7437.'
    PLEASE_DROP_KEY = 'Pudota oma autonavain kaappiin'
    PLEASE_CALL_CUSTOMER_SERVICE =' Soita mukautettuun palvelunumeroon'
    SHUT_DOOR_AFTER_THREE_DOT = ''
    SHUT_DOOR_AFTER = ''
    SHUT_DOOR = ''
    THANK_YOU_INFORM = 'Kiitos, saat meiltä ilmoituksen kun autosi korjaus on valmis'
    THANK_YOU = 'Kiitos, asioinnistasi Autoklinikalla ja turvallista kotimatkaa!'
    OPEN_BALANCE = 'Maksettava summa on'
    PAY = 'Maksaa'
    NEXT = 'Jatka'
    SIGN_IN = 'Kirjau sisää'
    SIGNUP = 'Kirjaudu'
    FULL = "Tämä kone on nyt täynnä, kokeile toista! Pahoittelemme aiheutunutta haittaa"
    
    TAKE_PIC = "Otta kuva"
    TRAINING_FACE = 'KOULUTUSKAMERA'
    WAIT = 'Odota muutaman minuutin kuluttua'
    
    YOUR_VEHICLE = 'Ajoneuvon kilven numero: '
    YOUR_PHONE_NUMBER = 'puhelinnumerosi: '
    
    LOGIN = 'KIRJAUDU SISÄÄN TÄSTÄ'
    PLEASE_FOLLOW_INSTRUCTION_PAYMENT = 'Maksa seuraamalla automaatin antamia ohjeita'
    PLEASE = 'Käsitellään...'
    PLEASE_WAIR_SUB_KEY ='Odota korvaavan ajoneuvon avainta'
    PLEASE_DROP_SUB_KEY ='Pudota korvaava avain'
    PICK_UP_KEY =' poimia oma avain'
    TAKE_KEY_THREE_DOT = 'Ota autonavaimet avautuvasta lokerosta'
    TAKE_KEY = 'Ota autonavaimet avautuvasta lokerosta'
    PAYMENT_OK = 'Kiitos, maksu on hyväksytty'
    PAYMENT_FAILED =  'Maksu epäonnistui'
    FOR_USING =  ''
    NOT_CONNECT_INTERNET =  'Ei internet yhteyttä'
    NO_CAMERA = 'Emme löydä kamerasi'
    TRY_AGAIN =  'Epäonnistui, yritä uudelleen!'
    HARDWARE_ERROR =  'Laitteistovirhe'
    DOOR_WILL_CLOSE =  'Luukku sulkeutuu'
    DOOR_OPENING =  'Odota hetki...'
    REG_PLATE ='Ajoneuvon rekisterikilpi on '
    SUB_CAR ='Sinulla on korvaava ajoneuvo'
    SIGN_UP = 'VIRALLINEN ILMOITTAUTUMISLOMAKE'
    SECOND =  'sekunnin kuluttua.'
    SECONDS =  'sekunnin kuluttua.'
    START = 'Aloita'
