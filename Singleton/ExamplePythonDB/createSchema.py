import sqlite3
from sqlite3 import Error
from connect import Database

"""
class 

"""
class ManipulateSchema(object):
    def __init__(self):
        self.db = Database()
    
    def __del__(self):
        self.db.connect().close()

    def create_table(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        print("Object created: ", cursor)
        try:
            #cursor.execute("DROP TABLE IF EXISTS formulario")
            cursor.execute('''CREATE TABLE IF NOT EXISTS formulario (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                fullname TEXT NOT NULL,
                cpf VARCHAR(11) NOT NULL,
                email TEXT,
                city TEXT NOT NULL,
                uf VARCHAR(2) NOT NULL,
                date_create DATE NOT NULL
            );''')
            #print('Query executed with success!')
        except Error as e:
            print(f'Error: {e}')
        finally:
            conn.commit()

    def drop_db(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("DROP TABLE IF EXISTS formulario")
        except Error as e:
            print(f'Error: {e}')
        finally:
            conn.commit()