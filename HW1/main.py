# this is HW1

# insert into users (firstname, lastname, email) values
# ('john', 'doe', 'johndoe@me.com')

import mysql.connector
from mysql.connector import Error


def create_con(hostname, username, userpw, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=userpw,
            database=dbname
        )
        print("success")
    except Error as e:
        print(f'the error {e} occurred')
    return connection

def display_menu():
    print("MENU")
    print("a - Add travel log")
    print("d - Remove travel log")
    print("u - Update travel log")
    print("o - Output entire log in console")
    print("s - Save travel log to database")
    print("q - Quit")
    user_select = input("Please select from MENU:\n")
    return user_select

def execute_menu(user_input):
    if user_input == "o":
        conn = create_con('cis3368fall.ctbnutpeyolk.us-east-1.rds.amazonaws.com', 'admin', 'admin123', 'cis3368')
        cursor = conn.cursor(dictionary=True)
        sql = 'select * from users'
        cursor.execute(sql)
        rows = cursor.fetchall()
        for user in rows:
            print(user)


user_input = display_menu()
execute_menu(user_input)




