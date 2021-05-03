from Subscriber import *
from NewEvent import *

# observer concrete 2
class SMSSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
        self.listOfNumbers = []

    def addNewNumber(self, number):
        self.listOfNumbers.append(number)

    def sendSMS(self):
        for number in self.listOfNumbers:
            print('Sending message to: ', number)

    def update(self):
        print(type(self).__name__, ' :: ', self.publisher.getEvent())
        self.sendSMS()
