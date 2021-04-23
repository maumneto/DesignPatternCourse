import sqlite3

'''Class Singleton  
    @name: Singleton
    @description: This class contains the Singleton implement
    @methods
        - __call__
'''
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

'''Class Database  
    @name: Database
    @description: Metaclass of Singleton and responsable to connect to the database
    @methods
        - connect
'''
class Database(metaclass=Singleton):
    def __init__(self):
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("database.db")
        return self.connection
