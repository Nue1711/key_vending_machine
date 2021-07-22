# https://github.com/timofurrer/observable

from observable import Observable

class ObservableTrigger:
    __instance = None

    def __init__(self):
        if ObservableTrigger.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ObservableTrigger.__instance = Observable()

    @staticmethod
    def getInstance():
        if ObservableTrigger.__instance == None:
            ObservableTrigger()
        return ObservableTrigger.__instance