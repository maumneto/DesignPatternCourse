from NewEvent import *
from Subscriber import *
from EmailSubscriber import *
from SMSSubscriber import *

class Main:
    def main(self):
        new_event = NewEvent()

        for Subscribers in [EmailSubscriber, SMSSubscriber]:
            Subscribers(new_event)
        print('Welcome!\nEnter with the hour and the minute of the event!')
        hour = int(input('hour: '))
        minutes = int(input('minutes: '))
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