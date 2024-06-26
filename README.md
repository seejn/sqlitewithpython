### Sqlite with Python

## cursor
- returns:
    cursor

## commit
- description:
    commit the query execution

## close
- description: 
    close the connection

## commit_and_close
- description:
    commit the query execution then close the connection

## create_table
- parameters:
    - table_name: name of a table to create
    - fields_in_tuple: fields to create in table required in tuple
- description:
    - creates a table in database
- returns:
    - None

## rename_table
- parameters: 
    - curr_table: name of table to rename
    - new_table: name of new table name
- description:
    - renames the table
- returns:
    - None

## add_new_column
- parameters: 
    - table_name: table to add new column at
    - new_column: name of column to add
    - definition: datatype and contraints of new table
- description:
    - adds new column to the table
- returns:
    - None

## rename_column
- parameters: 
    - table_name: name of table containing the column to rename
    - curr_column: current name of column
    - new_name: new name of column
- description:
    - renames column in a table
- returns:
    - None

## drop_table
- parameters:
    - table_name: name of a table to drop
- description:
    - drops the table
- returns:
    - None

## drop_tables
- parameters:
    - tables: takes tables in tuple
- description:
    - drops multiple tables at once
- returns:
    - None

## show_tables
- description: 
    - displays all the tables in database
- returns:
    - None

## insert_data
- parameters: 
    - table_name: name of table to insert data at
    - data: data to insert
        - data needs to be in key: value pair [ dictionary ]  
- description:
    - adds new column to the tables
- returns:
    - None

## insert_multiple_data
- parameters: 
    - table_name: name of table to insert data at
    - data: data to insert
        - data needs to be list of dictionary 
- description:
    - adds multiple data to the table
- returns:
    - None

## select_where
- parameters: 
    - table_name: name of table to get data from
    - condition: condition query to select data
- description:
    - selects data from table with given condition
- returns:
    - result: fetched data from the table

## get_data
- parameters:
    - table_name: name of table to get data from
    - fields: columns in table consisting of data
        - default (*): selects all fields if fields is not passed
    - id: id of row to select 
        - default (None): selects all row if id is not passed
- description:
    - can fetch all data and data based on id            
- returns:
    - result: data fetched is converted to list
        

## update_data
- parameters:
    - table_name: name of table to update data
    - fields: columns where data to be updated
        - fields can be in tuple or list
        - eg: ('field1', 'field2' ... 'fieldn')
    - new_data:  new_values to overwrite
        - values respective to fields defined
        - eg: ('value1', 'value2' ... 'valuen', id)
        - last element must be id for selection (mandatory)
        - for updating single row, new_data type: tuple
        - for updating multiple row, new_data: list of tuple
- description:
    - update the values of row/rows in table            
- returns:
    - None

## delete_data
- parameters:
    - table_name: name of table to delete data from
    - id: id of row to delete
        - default (None): deletes every row in a table
        - type(id) -> int: deletes the passed id row
        - type(id) -> list: multiple ids and deletes specified id's row
definition:
    - deletes data from table
- returns:
    - None