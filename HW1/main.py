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


def main(my_dict, count):
    user_select = display_menu()
    if user_select == "a":
        year = input("Please enter year (YYYY format):\n")
        comment = input("Please enter comment (256 max char limit):\n")
        revisit = input("Please enter revisit (256 max char limit):\n")
        count += 1
        if 1 in my_dict.keys():
            my_dict2 = {
                count: 'id',
                year: 'year',
                comment: 'comment',
                revisit: 'revisit'
            }
            my_dict.update(my_dict2)
        else:
            my_dict = {
                count: 'id',
                year: 'year',
                comment: 'comment',
                revisit: 'revisit'
            }
        print(my_dict)
        return main(my_dict, count)
    elif user_select == "d":
        main()
    elif user_select == "u":
        main()
    elif user_select == "o":
        print(my_dict)
    elif user_select == "s":
        conn = create_con('cis3368fall.ctbnutpeyolk.us-east-1.rds.amazonaws.com', 'admin', 'admin123', 'cis3368')
        cursor = conn.cursor()
        columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in my_dict.keys())
        rows = ', '.join("'" + str(x).replace('/', '_') + "'" for x in my_dict.values())
        sql = 'insert into %s (%s) values (%s);' % ("log", columns, rows)
        cursor.execute(sql)
        conn.commit()
        conn.close()
        main()
    elif user_select == "q":
        quit()
    else:
        print("incorrect selection, please try again")
        main(count)


count = 0
my_dict = dict()
main(my_dict, count)
