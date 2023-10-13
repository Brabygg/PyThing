import os
import sqlite3 as sql

def main():

    active = True
    while active:
        list_table()

        cnotine = input("Would you like to add another tower to the list?\n[1 - Yes; 2 - No]\n")
        if cnotine != "1":
            active = False
        
        if active:
            add_to_table()

def add_to_table():
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    name = input('What is the tower\'s name?\n')
    city = input('Where is it located?\n')
    collapsed = int(input('Has it been destoyed?\n'))
    status = input('Any additional notes?\n')

    connection = sql.connect('towers.db')
    cursor = connection.cursor()
    insert_query = f'''INSERT INTO towers (name, city, collapsed, status)
                    VALUES ('{name}', '{city}', {collapsed}, '{status}')'''
    
    cursor.execute(insert_query)
    connection.commit()
    connection.close()

def list_table():
    os.system('cls' if os.name == 'nt' else 'clear')

    connection = sql.connect('towers.db')
    cursor = connection.cursor()
    select_query = '''SELECT * FROM towers ORDER BY name'''

    cursor.execute(select_query)
    data = cursor.fetchall()

    for entry in data:
        print(f"ID {entry[0]}: {entry[1]}, {entry[2]}, {'DESTROYED, ' if entry[3] == 1 else ''}{f'notes: {entry[4]}' if entry[4] != None else 'NO NOTES'}")

    cursor.close()
    connection.close()

main()