class Singleton(object):
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print('Calling __init__ method...')
        else:
            print('The instance is already created: ', self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
             cls.__instance = Singleton()
        return cls.__instance


object1 = Singleton()
print('Object created: ', object1.getInstance())
object2 = Singleton()
print('Object created: ', object2.getInstance())