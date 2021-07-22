class Language():
    EN = 1  # English 
    FI = 2  # Finnish (default)

    __instance = FI

    @staticmethod
    def setLanguage(language: int):
        Language.__instance = language
    
    @staticmethod
    def getLanguage():
        return Language.__instance
