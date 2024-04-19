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
def main():
    conn = sqlite3.connect("test.db")
    db = SqliteDB(conn)

    tables = ("users","user") # tables in tuple
    table_name = "users"
    fields = ('id INTEGER PRIMARY KEY AUTOINCREMENT', 'name TEXT', 'email TEXT')

    # db.create_table(table_name, fields)

    # db.drop_table(table_name)

    # db.drop_tables(tables)

    # db.show_tables()

    db.close()
    # 
if __name__ == "__main__": # dunder
    main()