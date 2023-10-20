import os
import sqlite3 as sql

def connect_to_database(db):
    connection = sql.connect(db)
    cursor = connection.cursor()
    return connection, cursor

def close_connection(connection, cursor):
    try:
        cursor.close()
        connection.close()
        return 0
    except:
        return 1

def create_table(cursor, connection, name):
    try:
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {name} (
                        id INTEGER PRIMARY KEY,
                        native STRING NOT NULL,
                        trans STRING NOT NULL)""")
        connection.commit()
        return 0
    except:
        return 1
    
def drop_table(cursor, connection, name):
    try:
        cursor.execute(f"DROP TABLE {name}")
        connection.commit()
        return 0
    except:
        return 1

def add_to_table(cursor, connection, db, native, trans):
    try:
        cursor.execute(f"""INSERT INTO {db} (native, trans)
                       VALUES ('{native}', '{trans}')""")
        connection.commit()
        return 0
    except:
        return 1
    
def remove_from_table(cursor, connection, db, id):
    #try:
        cursor.execute(f"""CREATE TABLE temp (
                        id INTEGER PRIMARY KEY,
                        native STRING NOT NULL,
                        trans STRING NOT NULL)""")
        cursor.execute(f"DELETE FROM {db} WHERE id={id}")
        cursor.execute(f"SELECT * FROM {db}")
        for data in cursor:
            cursor.execute(f"""INSERT INTO temp (native, trans)
                            VALUES ('{data[1]}', '{data[2]}')""")
        cursor.execute(f"DROP TABLE {db}")
        cursor.execute(f"""ALTER TABLE temp
                        RENAME TO {db}""")
        connection.commit()
        return 0
    #except:
        #return 1
    
def edit_value(cursor, connection, db, id, native, trans):
    try:
        cursor.execute(f"""UPDATE {db}
                        SET native='{native}', trans='{trans}'
                        WHERE id={id}""")
        connection.commit()
        return 0
    except:
        return 1
    
def list_all_tables(cursor):
    tables = []

    try:
        cursor.execute("""SELECT name FROM sqlite_schema
                       WHERE type='table'
                       ORDER BY name""")
        for table in cursor:
            tables.append(table)
        return tables
    except:
        return []

def list_table_entries(cursor, db):
    entries = []

    try:
        cursor.execute(f"""SELECT * FROM {db}
                        ORDER BY native""")
        for entry in cursor:
            entries.append(entry)
        return entries
    except:
        return []