class Subject:
    def __init__(self):
        self._observers = []

    def notifyAll(self):
        for observer in self._observers:
            observer.update(self)

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError as error:
            print(error)
    

class SenderEmail(Subject):
    def __init__(self, email=''):
        Subject.__init__(self)
        self.emails = []

    def addNewEmail(self, email):
        self.emails.append(email)
        self.notifyAll()

    def sendEmail(self):
        for email in self.emails:
            print('Enviando e-mail para: ', email)

class ObserverEvent1:
    def update(self, subject):
        print('ObserverEvent1: ')
        subject.sendEmail()

if __name__ == '__main__':
    obj1 = SenderEmail()
    obj2 = SenderEmail()

    v1 = ObserverEvent1()

    obj1.attach(v1)
    obj1.addNewEmail('mauricio@provedor.com')
    obj1.addNewEmail('joao@provedor.com')
    obj1.addNewEmail('rafael@provedor.com')