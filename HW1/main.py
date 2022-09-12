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
    if user_input == "a":
        del_fname = input("Please enter first name:\n")
        del_lname = input("Please enter last name:\n")
        del_user_email = input("OPTIONAL: Please enter email name:\n")
        conn = create_con('cis3368fall.ctbnutpeyolk.us-east-1.rds.amazonaws.com', 'admin', 'admin123', 'cis3368')
        cursor = conn.cursor()
        sql = 'insert into users (firstname, lastname, email) values (%s, %s, %s)'
        data = (del_fname, del_lname, del_user_email)
        cursor.execute(sql, data)
        conn.commit()
        conn.close()
        display_menu()
    elif user_input == "d":
        fname = input("Please enter first name:\n")
        lname = input("Please enter last name:\n")
        user_email = input("OPTIONAL: Please enter email name:\n")
        conn = create_con('cis3368fall.ctbnutpeyolk.us-east-1.rds.amazonaws.com', 'admin', 'admin123', 'cis3368')
        cursor = conn.cursor()
        sql = 'select * from users'
        cursor.execute(sql)
        sql1 = 'insert into users (firstname, lastname, email) values (%s, %s, %s)'
        data = (fname, lname, user_email)
        cursor.execute(sql1, data)
        conn.commit()
        conn.close()
        display_menu()
    elif user_input == "o":
        conn = create_con('cis3368fall.ctbnutpeyolk.us-east-1.rds.amazonaws.com', 'admin', 'admin123', 'cis3368')
        cursor = conn.cursor(dictionary=True)
        sql = 'select * from users'
        cursor.execute(sql)
        rows = cursor.fetchall()
        for user in rows:
            print(user)
        conn.close()
    elif user_input == 'q':
        quit()



def main():
    user_input = display_menu()
    execute_menu(user_input)
    main()


main()
