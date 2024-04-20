class SqliteDB:
    
    def __init__(self, conn):
        self.__conn = conn
        self.__cursor = conn.cursor()

    # decorator
    def handle_exception(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception  as e:
                print(f"Exception (!!! {e.args[0]} !!!)")
                print("\n")
                return e.args[0]

        return wrapper
    
    # database methods
    def cursor(self):
        '''
            return:
                cursor
        '''
        return self.__cursor
    
    def commit(self):
        '''
        description:
                commit the query execution 
        '''
        self.__conn.commit()

        return
    
    def close(self):
        '''
        description: 
            close the connection
        '''
        self.__conn.close()
        
        return


    def commit_and_close(self):
        '''
        description:
            commit the query execution then close the connection
        '''
        self.__conn.commit()
        self.__conn.close()

        return

    # DATA DEFINITION: CREATE TABLE, ALTER TABLE, RENAME COLUMN, DROP TABLE, SHOW TABLE
    @handle_exception
    def create_table(self, table_name, fields_in_tuple):
        '''
        parameters:
            table_name: name of a table to create
            fields_in_tuple: fields to create in table required in tuple

        description:
            creates a table in database

        returns:
            None
        '''
        self.cursor().execute(f"CREATE TABLE IF NOT EXISTS {table_name}({', '.join(fields_in_tuple)})")
        self.commit()

        print(f"-- Created Table: {table_name} --")
        print("\n")

        return

    @handle_exception
    def drop_table(self, table_name):
        '''
        parameters:
            table_name: name of a table to drop

        description:
            drops the table
        '''
        self.cursor().execute(f"DROP TABLE IF EXISTS {table_name}")
        self.commit()

        print(f"-- Deleted Table: {table_name} --")
        print("\n")

        return

    def drop_tables(self, tables_in_tuple):
        '''
        parameter:
            tables: takes tables in tuple

        description:
            drops multiple tables at once
        '''
        for table in tables_in_tuple:
            self.drop_table(table)

        return

    def show_tables(self):
        '''
        description: 
            displays all the tables in database
        '''
        self.cursor().execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor().fetchall()

        print("Tables: ")

        if not len(tables):
            print("!!! No tables created !!!")
            return

        for table in tables:
            print(table[0])

        return

    # DATA MANIPULATION: INSERT, SELECT, UPDATE, DELETE
    @handle_exception
    def insert_data(self, table_name, values):
        sql = f"INSERT INTO {table_name}(name, email) VALUES(?, ?)"

        self.cursor().executemany(sql, values)
        self.commit()

        return

    # @handle_exception
    # def get_all_data(self, table_name, fields = '*'):

    #     if not fields  == '*':
    #         fields = ', '.join(fields)

    #     sql = f"SELECT {fields} FROM {table_name}"

    #     self.cursor().execute(sql);

    #     return list(self.cursor().fetchall())

    @handle_exception
    def get_data(self, table_name, fields = '*', id = None):
        
        '''
        parameters:

        description:
            can fetch all data and data based on id            
        
        returns:
            result: data fetched is converted to list
        '''

        if not fields  == '*':
            fields = ', '.join(fields)

        if not id:
            sql = f"SELECT {fields} FROM {table_name}"
            self.cursor().execute(sql)
            result = [list(value) for value in self.cursor().fetchall()]
        else:
            sql = f"SELECT {fields} FROM {table_name} where id = ?"
            self.cursor().execute(sql, (id, ))
            result = list(self.cursor().fetchone())

        return result

    @handle_exception
    def update_data(self, table_name, fields, new_data):
        
        if isinstance(new_data, list) or isinstance(new_data, tuple):
            
            fields = [f"{field} = ?" for field in fields]
            sql = f"UPDATE {table_name} SET {(', ').join(fields)} WHERE id = ?"

            if isinstance(new_data, list):
                self.cursor().executemany(sql, new_data)
            else:
                print(type(new_data))
                self.cursor().execute(sql, new_data)

            self.commit()

        else:
            print("datatype mismatched: type should be tuple or list")
            return

        return

    @handle_exception
    def delete_data(self, table_name, id = None):

        if not id:
            sql = f"DELETE FROM {table_name}"
            self.cursor().execute(sql)
        elif isinstance(id, int):
            sql = f"DELETE FROM {table_name} where id = ?"
            self.cursor().execute(sql, (id, ))
        else:
            sql = f"DELETE FROM {table_name} where id = ?"
            ids = [(i, ) for i in id]
            self.cursor().executemany(sql, ids)

        self.commit()
        
        return

    # initial testing database method

    def test_conn(self):
        self.cursor().execute("CREATE TABLE test(id INT, test TEXT)")
        self.commit()

        return
    

    