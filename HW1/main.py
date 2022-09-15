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


def execute_select(user_select):
    if user_select == "a":
        add_entry()
    elif user_select == "d":
        delete_entry()
    elif user_select == "u":
        update_entry()
    elif user_select == "o":
        output_log()
    elif user_select == "s":
        save_log()
    elif user_select == "q":
        quit()


def add_entry():
    year = input("Please enter year (YYYY format):\n")
    comment = input("Please enter comment (256 max char limit):\n")
    revisit = input("Please enter revisit (256 max char limit):\n")
    count += 1
    my_dict = {'id': count, 'year': year, 'comment': comment, 'revisit': revisit}
    print(my_dict)
    return my_dict, count


def delete_entry():
    display_menu()


def update_entry():
    display_menu()


def output_log():
    display_menu()


def save_log():
    conn = create_con('cis3368fall.ctbnutpeyolk.us-east-1.rds.amazonaws.com', 'admin', 'admin123', 'cis3368')
    cursor = conn.cursor()
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in my_dict.keys())
    rows = ', '.join("'" + str(x).replace('/', '_') + "'" for x in my_dict.values())
    sql = 'insert into %s (%s) values (%s);'("log", columns, rows)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    main()


def main():
    user_select = display_menu()
    execute_select(user_select)
    main()


main()
