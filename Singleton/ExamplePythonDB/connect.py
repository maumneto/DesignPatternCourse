import sqlite3
from sqlite3 import Error
from datetime import date

"""
class 

"""
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
"""
class 

"""
class Database(metaclass=Singleton):
    def __init__(self):
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("database.db")
            #self.cursorObject = self.connection.cursor()
        return self.connection
        #return self.cursorObject

# """
# class 

# """
# class ManipulatingDatabase(object):
#     def __init__(self):
#         self.db = Database()
    
#     def __del__(self):
#         self.db.connect().close()

#     def create_table(self):
#         conn = self.db.connect()
#         cursor = conn.cursor()
#         print("Object created: ", cursor)
#         try:
#             #cursor.execute("DROP TABLE IF EXISTS formulario")
#             cursor.execute('''CREATE TABLE IF NOT EXISTS formulario (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                 fullname TEXT NOT NULL,
#                 cpf VARCHAR(11) NOT NULL,
#                 email TEXT,
#                 city TEXT NOT NULL,
#                 uf VARCHAR(2) NOT NULL,
#                 date_create DATE NOT NULL
#             );''')
#             #print('Query executed with success!')
#         except Error as e:
#             print(f'Error: {e}')
#         finally:
#         #     conn.commit("DROP TABLE IF EXISTS formulario")

#     def drop_db(self):
#         conn = self.db.connect()
#         cursor = conn.cursor()
#         try:
#             cursor.execute("DROP TABLE IF EXISTS formulario")
#         except Error as e:
#             print(f'Error: {e}')
#         finally:
#             conn.commit()

    
#     def read_data(self):
#         result = None
#         conn = self.db.connect()
#         cursor = conn.cursor()
#         try:
#             cursor.execute("SELECT * FROM formulario;")
#             result = cursor.fetchall()
#         except Error as e:
#             print(f'Error: {e}')
#         finally:
#             return result

#     def insert_data(self, name, cpf, email, city, uf, date_create):
#         insert_query = '''INSERT INTO formulario (fullname, cpf, email, city, uf, date_create) 
#                     VALUES (?,?,?,?,?,?);'''
#         tupla = [name, cpf, email, city, uf, date_create]
#         conn = self.db.connect()
#         cursor = conn.cursor()
#         try:
#             cursor.execute(insert_query, tupla)
#             print('Insert data with success!')
#         except Error as e:
#             print(f'Error: {e}')
#         finally:
#             conn.commit()

#     def update_data(self, id):
#         update_query = f'''UPDATE formulario
#                         SET fullname = ?, cpf = ?, email = ?, city = ?, uf = ?, date_create = ?
#                         WHERE id = {id};'''
#         conn = self.db.connect()
#         cursor = conn.cursor()
#         # novos dados
#         name = input('Name: ')
#         cpf = input('CPF: ')
#         email = input('E-mail: ')
#         city = input('City: ')
#         uf = input('UF: ')
#         date_create = date.today()
#         tupla = [name, cpf, email, city, uf, date_create]
#         try:
#             cursor.execute(update_query, tupla)
#             print('Successful Updata!')
#         except Error as e:
#             print(f'Error: {e}')
#         finally:
#             conn.commit()
    
#     def delete_data(self, id):
#         delete_query = f'''DELETE FROM formulario
#                         WHERE id = {id};'''
#         conn = self.db.connect()
#         cursor = conn.cursor()
#         try:
#             cursor.execute(delete_query)
#             print('Deleted data')
#         except Error as e:
#             print(f'Error: {e}')
#         finally:
#             conn.commit()

# """
# class 

# """
# class Main(object):
#     def main(self):
#         db = ManipulatingDatabase()
#         # db.create_table()
#         # db2 = ManipulatingDatabase()
#         # db2.create_table()
        
#         print('Welcome to the Singleton Example')
#         while True:
#             print(' ')
#             option = int(input('Choose one of these options:\n1 - Insert\n2 - Read\n3 - Update\n4 - Delete\n5 - Exit\nResp: '))
#             if option == 1:
#                 name = input('name: ')
#                 cpf = input('CPF: ')
#                 email = input('E-mail: ')
#                 city = input('City: ')
#                 uf = input('UF: ')
#                 date_create = date.today()
#                 db.insert_data(name, cpf, email, city, uf, date_create)
#             elif option == 2:
#                 alldata = db.read_data()
#                 for row in alldata:
#                     print(row)
#             elif option == 3:
#                 id = int(input('ID: '))
#                 db.update_data(id)
#             elif option == 4:
#                 id = int(input('ID: '))
#                 db.delete_data(id)
#             elif option == 5:
#                 break
#             else:
#                 print('No valid options selected!')



# if __name__ == '__main__':
#     m = Main()
#     m.main()
