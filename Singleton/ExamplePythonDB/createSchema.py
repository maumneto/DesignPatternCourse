import sqlite3
from sqlite3 import Error
from connect import Database

'''Class ManipulateSchema  
    @name: ManipulateSchema
    @description: This class create and drop the schema of database
    @methods
        - create_table
        - drop_db
'''
class ManipulateSchema(object):
    '''@Constructor
        Initialize the object for manipulating the database
    '''
    def __init__(self):
        self.db = Database()
    '''@Destructor
        Close the connection after use the object
    '''
    def __del__(self):
        self.db.connect().close()

    '''@create_table method
        Method that create the schema of the database
        Parameters
            - void
        Return
            - void                   
    '''
    def create_table(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        print("Object created: ", cursor)
        try:
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
    '''@drop_table method
        Method that drop the schema of the database
        Parameters
            - void
        Return
            - void                   
    '''
    def drop_table(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("DROP TABLE IF EXISTS formulario")
            print('Table successfully deleted!')
        except Error as e:
            print(f'Error: {e}')
        finally:
            conn.commit()