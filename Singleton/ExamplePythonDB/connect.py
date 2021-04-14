import sqlite3
from sqlite3 import Error

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("Singleton/ExamplePythonDB/database.db")
            self.cursorObject = self.connection.cursor()
        return self.cursorObject


# class ManipulatingDatabase(object):

#     def execute_query(self, query):
#         db = Database()
#         cursor = db.connect()
#         print(cursor)
#         try:
#             cursor.execute(query)
#             print('Query executed with success!')
#         except Error as e:
#             print(f'Error: {e}')
#         finally:
#             cursor.close()
