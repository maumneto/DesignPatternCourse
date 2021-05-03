import time

# class Subject 
class NewEvent:
    def __init__(self):
        self.__subscribers = []
        self.__message = ''
    
    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self, subscriber):
        self.__subscribers.pop()

    def showSubscribers(self):
        return [type(sub).__name__ for sub in self.__subscribers]

    def notifyAll(self):
        for sub in self.__subscribers:
            sub.update()
    
    def addMessage(self, message=''):
        self.__message = message

    def getEvent(self):
        return "A wild event appears! Message: " + self.__message
    
    def AddEventTime(self, hour=00, minutes=00, seconds = 00):
        now = time.localtime()
        flag = False
        if (now.tm_hour == hour and now.tm_min == minutes):
            self.notifyAll()
            flag = True
        return flag

    