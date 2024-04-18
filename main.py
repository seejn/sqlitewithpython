import sqlite3
from database.SqliteDB import SqliteDB

def main():
    conn = sqlite3.connect("test.db")
    db = SqliteDB(conn)

    table_name = "user"
    tables = ("",) # talbes in tuple
    fields = ("id INT", "name TEXT", "email TEXT")

    db.create_table(table_name, fields)

    # db.drop_table(table_name)

    # db.drop_tables(tables)

    db.show_tables()
    db.close()
    # 
if __name__ == "__main__": # dunder
    main()