from sqlite3 import Error
from connect import Database

class ManipulatingDatabase(object):

    def execute_query(self, query):
        db = Database()
        cursor = db.connect()
        print(cursor)
        try:
            cursor.execute(query)
            print('Query executed with success!')
        except Error as e:
            print(f'Error: {e}')
        finally:
            cursor.close()