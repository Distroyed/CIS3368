import mysql.connector
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query
import creds

my_creds = creds.Creds()
conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)

# create new entry and add it to the table
# query = "INSERT INTO users (firstname, lastname) VALUES ('Thomas', 'Edison')"
# execute_query(conn, query)

# select all users from the table
select_users = "SELECT * FROM users"
users = execute_read_query(conn, select_users)
for user in users:
    print(user["firstname"] + " has the lastname: " + user["lastname"])

# add a table for invoices (if you dynamically add tables, you need to dynamically delete)
create_inv_table = """
CREATE TABLE IF NOT EXISTS invoices(
id INT AUTO_INCREMENT, 
amount INT, 
description VARCHAR(255) NOT NULL, 
user_id INTEGER UNSIGNED NOT NULL, 
FOREIGN KEY fk_user_id(user_id) REFERENCES users(id), 
PRIMARY KEY (id)
)"""

execute_query(conn, create_inv_table)

# add invoice record to invoice table
invoice_from_user = 1
invoice_amount = 50
invoice_description = "Harry Potter Books"

query = "INSERT INTO invoices (amount, description, user_id) VALUES (%s, '%s', %s)" % (invoice_amount,
                                                                                       invoice_description,
                                                                                       invoice_from_user)
# execute_query(conn, query)

# update invoice record
new_amount = 30
update_invoice_query = """
UPDATE invoices
SET amount = %s
WHERE id = 1""" % new_amount

# execute_query(conn, update_invoice_query)

# delete invoice record from invoice table
invoice_to_delete = 1
delete_statement = "DELETE FROM invoices WHERE id = %s" % invoice_to_delete
# execute_query(conn, delete_statement)

# delete invoices table
delete_table_statement = "DROP TABLE invoices"
execute_query(conn, delete_table_statement)
