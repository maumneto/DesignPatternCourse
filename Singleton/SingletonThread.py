import threading
import sqlite3

lock = threading.Lock()

'''
'''
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with lock:
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

    print('Object 1: ', db1)
    print('Object 2: ',  db2)
