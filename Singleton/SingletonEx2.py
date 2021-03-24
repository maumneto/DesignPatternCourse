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


singleton = Singleton()
print('Object created: ', singleton.getInstance())
object1 = Singleton()