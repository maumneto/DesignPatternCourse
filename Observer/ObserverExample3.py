
'''
@class Subject: 
'''
class Subject:
    def __init__(self):
        self.__observers = []

    def attach(self, observer):
        self.__observers.append(observer)

    def detach(self, observer):
        self.__observers.remove(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.update(self, *args, **kwargs)

class FirstObserver:
    def __init__(self, subject):
        subject.attach(self)

    def update(self, subject, *args):
        print('First Observer has received ', args, ' from ', subject)


class SecondObserver:
    def __init__(self, subject):
        subject.attach(self)

    def update(self, subject, *args):
        print('Second Observer has received ', args, ' from ', subject)


class Main:
    def main(self):
        subject = Subject()
        observer1 = FirstObserver(subject)
        observer2 = SecondObserver(subject)
        subject.notifyAll('A new notification appears...')

if __name__ == '__main__':
    m = Main()
    m.main()
