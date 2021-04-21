import sqlite3
from sqlite3 import Error
from datetime import date
from connect import Database

"""
class 

"""
class ManipulatingDatabase(object):
    def __init__(self):
        self.db = Database()
    
    def __del__(self):
        self.db.connect().close()
    
    def read_data(self):
        result = None
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM formulario;")
            result = cursor.fetchall()
        except Error as e:
            print(f'Error: {e}')
        finally:
            return result

    def insert_data(self, name, cpf, email, city, uf, date_create):
        insert_query = '''INSERT INTO formulario (fullname, cpf, email, city, uf, date_create) 
                    VALUES (?,?,?,?,?,?);'''
        tupla = [name, cpf, email, city, uf, date_create]
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(insert_query, tupla)
            print('Insert data with success!')
        except Error as e:
            print(f'Error: {e}')
        finally:
            conn.commit()

    def update_data(self, id):
        update_query = f'''UPDATE formulario
                        SET fullname = ?, cpf = ?, email = ?, city = ?, uf = ?, date_create = ?
                        WHERE id = {id};'''
        conn = self.db.connect()
        cursor = conn.cursor()
        # novos dados
        name = input('Name: ')
        cpf = input('CPF: ')
        email = input('E-mail: ')
        city = input('City: ')
        uf = input('UF: ')
        date_create = date.today()
        tupla = [name, cpf, email, city, uf, date_create]
        try:
            cursor.execute(update_query, tupla)
            print('Successful Updata!')
        except Error as e:
            print(f'Error: {e}')
        finally:
            conn.commit()
    
    def delete_data(self, id):
        delete_query = f'''DELETE FROM formulario
                        WHERE id = {id};'''
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(delete_query)
            print('Deleted data')
        except Error as e:
            print(f'Error: {e}')
        finally:
            conn.commit()