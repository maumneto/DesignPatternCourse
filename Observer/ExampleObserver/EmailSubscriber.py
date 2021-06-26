from Subscriber import *
from NewEvent import *

# observer concrete 1
class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
        self.listOfEmails = []

    def addNewEmail(self, email):
        self.listOfEmails.append(email)

    def sendEmail(self):
        for email in self.listOfEmails:
            print('Sending message to: ', email)

    def update(self):
        print(type(self).__name__, ' :: ',self.publisher.getEvent())
        self.sendEmail()