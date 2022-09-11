# this is HW1

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
