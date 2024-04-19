import sqlite3
from database.SqliteDB import SqliteDB

def insert(db):
    # values needs to be list for single or multiple 
    values = [
        ("Sijan1", "seejnmaharjan@gmail.com"),
        ("Sijan2", "seejnmaharjan@gmail.com"),
        ("Sijan3", "seejnmaharjan@gmail.com"),
        ("Sijan4", "seejnmaharjan@gmail.com"),
    ]

    table_name = "users"
    db.insert_data(table_name, values)

    return

def get_data(db):
    table_name = "users"
    fields = ('name','id')
    id = 6

    return db.get_data(table_name, fields)

def delete_data(db):
    table_name = "users"
    id = [19, 21]

    db.delete_data(table_name, id)

def main():
    conn = sqlite3.connect("test.db")
    db = SqliteDB(conn)

    tables = ("users","user") # tables in tuple
    table_name = "users"
    fields = ('id INTEGER PRIMARY KEY AUTOINCREMENT', 'name TEXT', 'email TEXT')

    '''
    DATA DEFINITION METHODS
    '''

    # db.create_table(table_name, fields)

    # db.drop_table(table_name)

    # db.drop_tables(tables)

    # db.show_tables()


    '''
    DATA MANIPULATION METHODS
    '''

    # insert(db)

    print(get_data(db))

    # delete_data(db)

    db.close()
    # 
if __name__ == "__main__": # dunder
    main()