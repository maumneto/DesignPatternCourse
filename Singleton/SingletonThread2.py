import threading
import sqlite3

'''
'''
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
'''
'''
class Database(metaclass=Singleton):
    def __init__(self):
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("database.db")
        return self.connection

if __name__ == '__main__':
    db1 = Database()
    db2 = Database()
    
    ob1 = threading.Thread(db1, args=(1,))
    ob1.start()
    ob2 = threading.Thread(db2, args=(1,))
    ob2.start()

    print('Object 1: ', ob1)
    print('Object 2: ',  ob2)

