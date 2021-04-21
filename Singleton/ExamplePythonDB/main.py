import sqlite3
from sqlite3 import Error
from datetime import date
from connect import Database
from manipulateDB import ManipulatingDatabase
"""
class 

"""
class Main(object):
    def main(self):
        db = ManipulatingDatabase()
        # db.create_table()
        # db2 = ManipulatingDatabase()
        # db2.create_table()
        
        print('Welcome to the Singleton Example')
        while True:
            print(' ')
            option = int(input('Choose one of these options:\n1 - Insert\n2 - Read\n3 - Update\n4 - Delete\n5 - Exit\nResp: '))
            if option == 1:
                name = input('name: ')
                cpf = input('CPF: ')
                email = input('E-mail: ')
                city = input('City: ')
                uf = input('UF: ')
                date_create = date.today()
                db.insert_data(name, cpf, email, city, uf, date_create)
            elif option == 2:
                alldata = db.read_data()
                for row in alldata:
                    print(row)
            elif option == 3:
                id = int(input('ID: '))
                db.update_data(id)
            elif option == 4:
                id = int(input('ID: '))
                db.delete_data(id)
            elif option == 5:
                break
            else:
                print('No valid options selected!')



if __name__ == '__main__':
    m = Main()
    m.main()