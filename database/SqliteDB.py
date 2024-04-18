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

    # DATA DEFINATION: CREATE TABLE, ALTER TABLE, RENAME COLUMN, DROP TABLE, SHOW TABLE
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
        self.cursor().execute(f"CREATE TABLE {table_name}{fields_in_tuple}") 
        self.commit()

        print(f"-- Created Table: {table_name} --")
        print("\n")

        return

    @handle_exception
    def drop_table(self, table_name):
        '''
        parameters:
            table_name: name of a table to drop
        '''
        self.cursor().execute(f"DROP TABLE {table_name}")
        self.commit()

        print(f"-- Deleted Table: {table_name} --")
        print("\n")

        return

    def drop_tables(self, tables_in_tuple):
        '''
        parameter:
            tables: takes tables in tuple
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

    # DATA MANIPULATION 


    # initial testing database method

    def test_conn(self):
        self.cursor().execute("CREATE TABLE test(id INT, test TEXT)")
        self.commit()

        return
    

    