class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

# creating the object1
object1 = Singleton()
print('Object 1: ', object1)
# creating the object2
object2 = Singleton()
print('Object 2: ', object2)