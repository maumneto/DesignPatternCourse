from abc import ABCMeta, abstractmethod

# interface observer
class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass