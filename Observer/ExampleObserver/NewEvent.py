from datetime import datetime
import time
from abc import ABCMeta, abstractmethod
import asyncio

# class Subject 
class NewEvent:
    def __init__(self):
        self.__subscribers = []
    
    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self, subscriber):
        self.__subscribers.pop()

    def showSubscribers(self):
        return [type(sub).__name__ for sub in self.__subscribers]

    def notifyAll(self):
        for sub in self.__subscribers:
            sub.update()
    
    def getEvent(self):
        return "A wild event appears..."
        
    
    def AddEventTime(self, hour=00, minutes=00, seconds = 00):
        now = time.localtime()
        if (now.tm_hour == hour and now.tm_min == minutes):
            print('Enter!')
            self.notifyAll()
        else:
            print('wait')

# interface observer
class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass

# observer concrete 1
class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getEvent())

# observer concrete 2
class SMSSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getEvent())


if __name__ == '__main__':
    new_event = NewEvent()

    for Subscribers in [EmailSubscriber, SMSSubscriber]:
        Subscribers(new_event)

    # year = int(input('year: '))
    # month = int(input('month: '))
    # day = int(input('day: '))
    hour = int(input('hour: '))
    minutes = int(input('minutes: '))
    seconds = int(input('minutes: '))

    new_event.AddEventTime(hour, minutes)
    new_event.notifyAll()

    print('Subscribers: ',  new_event.showSubscribers())