# this is HW1

# insert into users (firstname, lastname, email) values
# ('john', 'doe', 'johndoe@me.com')

import mysql.connector
from mysql.connector import Error


# from class
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


# menu function
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
        # this is my way of creating an auto-increment key
        # so that the user can easily identify what needs to be changed or deleted
        if 1 in my_dict.keys():
            my_dict2 = {
                count: [year, comment, revisit]
            }
            my_dict.update(my_dict2)
        else:
            my_dict = {
                count: [year, comment, revisit]
            }
        print(my_dict)
        return main(my_dict, count)
    elif user_select == "d":
        del_key = int(input("select id to delete (must be numeric):\n"))
        # looping through the dictionary to find the right to key to delete
        for key, value in list(my_dict.items()):
            if key == del_key:
                del my_dict[key]
        return main(my_dict, count)
    elif user_select == "u":
        update_key = int(input("Select id to update (must be numeric):\n"))
        # looping through the dictionary to find the right to key to change
        for key, value in list(my_dict.items()):
            if key == update_key:
                new_year = input("Please enter new year (YYYY format):\n")
                new_comment = input("Please enter new comment (256 max char limit):\n")
                new_revisit = input("Please enter in new revisit (256 max char limit):\n")
                my_dict[key] = [new_year, new_comment, new_revisit]
        return main(my_dict, count)
    elif user_select == "o":
        print(my_dict)
        return main(my_dict, count)
    elif user_select == "s":
        conn = create_con('cis3368fall.ctbnutpeyolk.us-east-1.rds.amazonaws.com', 'admin', 'admin123', 'cis3368')
        cursor = conn.cursor()
        for value in my_dict:
            print(my_dict[value][0])
            sql = "insert into log (year, comment, revisit) values (%s, %s, %s)"
            data = (my_dict[value][0], my_dict[value][1], my_dict[value][2])
            cursor.execute(sql, data)
            conn.commit()
        conn.close()
        return main(my_dict, count)
    elif user_select == "q":
        quit()
    else:
        print("incorrect selection, please try again")
        return main(my_dict, count)


###############
#  MAIN BODY  #
###############


count = 0
my_dict = dict()
main(my_dict, count)
