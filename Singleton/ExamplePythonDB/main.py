from manipulateDB import ManipulatingDatabase 

def main():
    db = ManipulatingDatabase()
    with open('Singleton/ExamplePythonDB/schema.sql', 'r') as file:
        sql = file.read()
        db.execute_query(sql)
    file.close()


    with open('Singleton/ExamplePythonDB/schema.sql', 'r') as file:
        sql = file.read()
        db.execute_query(sql)
    file.close()

if __name__ == '__main__':
    main()