import sqlite3
from sqlite3 import Error
from datetime import date
from connect import Database
from manipulateDB import ManipulateDatabase
from createSchema import ManipulateSchema

'''Class Main
    @name: Main
    @description: Main class that contains the choice of user options
    @methods:
        - main
'''
class Main(object):
    '''@Constructor
        Initialize the object for manipulating the database and the database schema
    '''
    def __init__(self):
        self.db = ManipulateDatabase()
        self.schema = ManipulateSchema()

    '''@main method
        Method that has the user choice logic
    '''
    def main(self): 
        print('Welcome to the Singleton Example')

        op = input('Do you want to keep the schema? [y/n]: ')
        op = op.lower()
        if (op == 'n'):
            self.schema.drop_table()
            self.schema.create_table()
        elif (op == 'y'):
            self.schema.create_table()
        else:
            print('No valid options selected!')
        
        while True:
            print(' ')
            option = int(input('Choose one of these options:\n1 - Insert\n2 - Read\n3 - Update\n4 - Delete\n5 - Exit\nResp: '))
            if option == 1:
                name = input('Name: ')
                cpf = input('CPF: ')
                email = input('E-mail: ')
                city = input('City: ')
                uf = input('UF: ')
                date_create = date.today()
                self.db.insert_data(name, cpf, email, city, uf, date_create)
            elif option == 2:
                alldata = self.db.read_data()
                if (alldata == None):
                    print('There is no record in the database!')
                for row in alldata:
                    print(row)
            elif option == 3:
                id = int(input('ID: '))
                self.db.update_data(id)
            elif option == 4:
                id = int(input('ID: '))
                self.db.delete_data(id)
            elif option == 5:
                break
            else:
                print('No valid options selected!')

if __name__ == '__main__':
    m = Main()
    m.main()