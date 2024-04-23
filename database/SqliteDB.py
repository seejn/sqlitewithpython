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
            returns:
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
    def rename_table(self, curr_table, new_table):
        '''
        parameters: 
            curr_table: name of table to rename
            new_table: name of new table

        description:
            renames the table

        returns:
            None
        '''
        sql = f"ALTER TABLE {curr_table} RENAME TO {new_table}"
        self.cursor().execute(sql)
        self.commit()
        
        return

    
    @handle_exception
    def add_new_column(self, table_name, new_column, definition):
        '''
        parameters: 
            table_name: table to add new column at
            new_column: name of column to add
            definition: datatype and contraints of new table

        description:
            adds new column to the table

        returns:
            None
        '''
        sql = f"ALTER TABLE {table_name} ADD COLUMN {new_column} {definition}"
        self.cursor().execute(sql)
        self.commit()
        
        return

    
    @handle_exception
    def rename_column(self, table_name, curr_name, new_name):
        '''
        parameters: 
            table_name: name of table containing the column to rename
            curr_column: current name of column
            new_name: new name of column

        description:
            renames column in a table

        returns:
            None
        '''
        sql = f"ALTER TABLE {table_name} RENAME COLUMN {curr_name} TO {new_name}"
        print(sql)
        self.cursor().execute(sql)
        self.commit()
        
        return

    @handle_exception
    def drop_table(self, table_name):
        '''
        parameters:
            table_name: name of a table to drop

        description:
            drops the table

        returns:
            None
        '''
        self.cursor().execute(f"DROP TABLE IF EXISTS {table_name}")
        self.commit()

        print(f"-- Deleted Table: {table_name} --")
        print("\n")

        return

    @handle_exception
    def drop_tables(self, tables_in_tuple):
        '''
        parameter:
            tables: takes tables in tuple

        description:
            drops multiple tables at once

        returns:
            None
        '''
        for table in tables_in_tuple:
            self.drop_table(table)

        return

    @handle_exception
    def show_tables(self):
        '''
        description: 
            displays all the tables in database
        
        returns:
            None
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
    def insert_data(self, table_name, data):
        '''
        parameters: 
            table_name: name of table to insert data at
            data: data to insert
                - data needs to be in key: value pair [ dictionary ] 

        description:
            adds new data to the table

        returns:
            None
        '''
        fields = ', '.join(list(data.keys()))
        values = list(data.values())
        sql = f"INSERT INTO {table_name}({fields}) VALUES(?, ?)"
        self.cursor().execute(sql, values)
        self.commit()
        
        return

    @handle_exception
    def insert_multiple_data(self, table_name, data):
        '''
        parameters: 
            table_name: name of table to insert data at
            data: data to insert
                - data needs to be list of dictionary 

        description:
            adds multiple data to the table

        returns:
            None
        '''
        for i in data:
            self.insert_data(table_name, i)
        return

    # @handle_exception
    # def get_all_data(self, table_name, fields = '*'):

    #     if not fields  == '*':
    #         fields = ', '.join(fields)

    #     sql = f"SELECT {fields} FROM {table_name}"

    #     self.cursor().execute(sql);

    #     return list(self.cursor().fetchall())

    @handle_exception
    def select_where(self, table_name, condition):
        '''
        parameters: 
            table_name: name of table to get data from
            condition: condition query to select data

        description:
            selects data from table with given condition

        returns:
            result: fetched data from the table
        '''
        sql = f"SELECT * FROM {table_name} WHERE {condition}"

        self.cursor().execute(sql)
        
        result = [list(value) for value in self.cursor().fetchall()]
        result = result[0] if len(result) == 1 else result

        self.commit()
        return result

    @handle_exception
    def get_data(self, table_name, fields = '*', id = None):
        '''
        parameters:
            table_name: name of table to get data from
            fields: columns in table consisting of data
                - default (*): selects all fields if fields is not passed
            id: id of row to select 
                - default (None): selects all row if id is not passed

        description:
            can fetch all data and data based on id            
        
        returns:
            result: data fetched is converted to list
                    - if no data found returns None
        '''
        if not fields  == '*':
            fields = ', '.join(fields)

        if id is not None and not id:
            result = None
        elif id is None:
            sql = f"SELECT {fields} FROM {table_name}"
            self.cursor().execute(sql)
            result = [list(value) for value in self.cursor().fetchall()]
        else:
            sql = f"SELECT {fields} FROM {table_name} where id = ?"
            self.cursor().execute(sql, (id, ))
            data = self.cursor().fetchone()
            result = list(data) if data else data 

        return result

    @handle_exception
    def update_data(self, table_name, fields, new_data):
        '''
        parameters:
            table_name: name of table to update data
            fields: columns where data to be updated
                - fields can be in tuple or list
                - eg: ('field1', 'field2' ... 'fieldn')
            new_data:  new_values to overwrite
                - values respective to fields defined
                    - eg: ('value1', 'value2' ... 'valuen', id)
                    - last element must be id for selection (mandatory)
                - for updating single row, new_data type: tuple
                - for updating multiple row, new_data: list of tuple

        description:
            update the values of row/rows in table            
        
        returns:
            None
        '''
        if isinstance(new_data, list) or isinstance(new_data, tuple):
            
            fields = [f"{field} = ?" for field in fields]
            sql = f"UPDATE {table_name} SET {(', ').join(fields)} WHERE id = ?"

            if isinstance(new_data, list):
                self.cursor().executemany(sql, new_data)
            else:
                self.cursor().execute(sql, new_data)

            self.commit()

        else:
            print("datatype mismatched: type should be tuple or list")
            return

        return

    @handle_exception
    def delete_data(self, table_name, id = None):
        '''
        parameters:
            table_name: name of table to delete data from
            id: id of row to delete
                default (None): deletes every row in a table
                type(id) -> int: deletes the passed id row
                type(id) -> list: multiple ids and deletes specified id's row
        definition:
            deletes data from table
        returns:
            None
        '''
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
    

    
