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

def get(db):
    table_name = "users"
    fields = ('name','id')
    id = 6

    return db.get_data(table_name)

def update(db):
    table_name = "users"

    # fields and new data can be in list or tuple
    fields = ('name', 'email')


    # last element must be id of row to update
    # eg: ('new_value', 'new_value', id_of_row_to_update)

    # for updating single value only, set in tuple
    single_data = ("seejn1", "seejn@gmail.com", 20)

    # for updating multiple values, set in list of tuples
    multiple_data = [
        ("seejn1", "seejn1@gmail.com", 20),
        ("seejn2", "seejn2@gmail.com", 22),
    ]

    return db.update_data(table_name, fields, single_data)

def delete(db):
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


    update(db)
    print(get(db))

    # delete(db)

    db.close()
    # 
if __name__ == "__main__": # dunder
    main()