from NewEvent import *
from Subscriber import *
from EmailSubscriber import *
from SMSSubscriber import *

class Main:
    def main(self):
        new_event = NewEvent()
        email_sub = EmailSubscriber(new_event)
        sms_sub = SMSSubscriber(new_event)

        print('Welcome!\nEnter with the hour and the minute of the event!')
        while True:
            op = int(input('1-Add email - 2-Add SMS - 3-Exit\nOption: '))
            if (op == 1):
                email = input('Email: ')
                email_sub.addNewEmail(email)
            elif (op == 2):
                sms = input('Phone number: ')
                sms_sub.addNewNumber(sms)
            elif (op == 3):
                print('All data was recorded!')
                break
            else:
                print('No option chosen!')
                break
            
        print('Make an appointment!')
        hour = int(input('Hour: '))
        minutes = int(input('Minutes: '))
        message = input('Say something: ')
        new_event.addMessage(message)
        print('Subscribers: ',  new_event.showSubscribers())
        print('')
        while True:
            flag = new_event.AddEventTime(hour, minutes)
            if flag:
                break

if __name__ == '__main__':
    m = Main()
    m.main()