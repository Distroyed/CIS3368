############
# MYSQL CODE
############

# two tables
# watches = extra credit using UUID
# watches1 = auto-increment INT

###################
# watches1 db table
###################

# create table watches1 (
# id int NOT NULL auto_increment,
# make varchar(25) NOT NULL,
# model varchar(25) NOT NULL,
# type varchar(25) NOT NULL,
# purchaseprice decimal(13,2) NOT NULL,
# salesprice decimal(13,2) NOT NULL,
# PRIMARY KEY (id)
# )

# INSERT EXAMPLE
# insert into watches1 (make, model, type, purchaseprice, salesprice)
# VALUES ('cartier', 'santos-dumont', 'quartz', 3200.00, 4000.00);

##################
# watches db table
##################

# create table watches (
# id binary(16) PRIMARY KEY,
# make varchar(25) NOT NULL,
# model varchar(25) NOT NULL,
# type varchar(25) NOT NULL,
# purchaseprice decimal(13,2) NOT NULL,
# salesprice decimal(13,2) NOT NULL
# );

# INSERT EXAMPLE
# insert into watches(id, make, model, type, purchaseprice, salesprice)
# values (UUID_TO_BIN(UUID()), 'rolex', 'oyster', 'mechanical', 8000.00, 10000.00),
# (UUID_TO_BIN(UUID()), 'cartier', 'large', 'mechanical', 5800.00, 6800.00),
# (UUID_TO_BIN(UUID()), 'br-x1', 'skeleton', 'mechanical', 400000.00, 480000.00),
# (UUID_TO_BIN(UUID()), 'garmin', 'fenix7', 'solar', 800.00, 899.99),
# (UUID_TO_BIN(UUID()), 'cartier', 'santos-dumont', 'quartz', 3200.00, 4000.00);


###########
# modules
###########


import flask
import json
import uuid
from json import JSONEncoder
from uuid import UUID
from flask import jsonify
from flask import request, flash
from sql import create_connection
from sql import execute_read_query
import creds


###########
# APIs
###########


# setting up app name
app = flask.Flask(__name__)
app.config["DEBUG"] = True

valid_tokens = {
    '880088'
}

@app.route('/', methods=['GET'])
def home():
    return "<h1> If you see this, they will grade </h1>"


# GET
@app.route('/api/watch', methods=['GET'])
def watch_all():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    sql = "SELECT * FROM watches1"
    watches1 = execute_read_query(conn, sql)
    return jsonify(watches1)


# PUT
@app.route('/api/watch', methods=['PUT'])
def update_watch():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    cursor = conn.cursor()
    request_data = request.get_json()
    change_id = request_data['id']
    change_make = request_data['make']
    change_model = request_data['model']
    change_type = request_data['type']
    change_purchase_price = request_data['purchaseprice']
    change_sales_price = request_data['salesprice']
    sql = "UPDATE watches1 SET make=%s, model=%s, type=%s, purchaseprice=%s, salesprice=%s WHERE id=%s"
    data = (change_make, change_model, change_type, change_purchase_price, change_sales_price, change_id)
    cursor.execute(sql, data)
    conn.commit()
    sql = "SELECT * FROM watches1"
    watches1 = execute_read_query(conn, sql)
    return jsonify(watches1)


# POST
@app.route('/api/watch', methods=['POST'])
def add_watch():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    cursor = conn.cursor()
    request_data = request.get_json()
    add_make = request_data['make']
    add_model = request_data['model']
    add_type = request_data['type']
    add_purchase_price = request_data['purchaseprice']
    add_sales_price = request_data['salesprice']
    sql = "INSERT INTO watches1 (make, model, type, purchaseprice, salesprice) VALUES (%s, %s, %s, %s, %s)"
    data = (add_make, add_model, add_type, add_purchase_price, add_sales_price)
    cursor.execute(sql, data)
    conn.commit()
    sql = "SELECT * FROM watches1"
    watches1 = execute_read_query(conn, sql)
    return jsonify(watches1)


# DELETE
@app.route('/api/watch/token/<token>', methods=['DELETE'])
def del_watch(token):
    for valid_token in valid_tokens:
        if token == valid_token:
            my_creds = creds.Creds()
            conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
            cursor = conn.cursor()
            request_data = request.get_json()
            del_id = request_data['id']
            sql = "DELETE FROM watches1 WHERE id=%s"
            data = (del_id,)
            cursor.execute(sql, data)
            conn.commit()
            sql = "SELECT * FROM watches1"
            watches1 = execute_read_query(conn, sql)
            return jsonify(watches1)
    return 'INVALID ACCESS TOKEN'


##############
# EXTRA CREDIT
##############


# GET
@app.route('/api/watch/xtra', methods=['GET'])
def xtra_watch_all():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    sql = "SELECT * FROM watches"
    watches = execute_read_query(conn, sql)
    return jsonify(watches)


# PUT
@app.route('/api/watch/xtra', methods=['PUT'])
def xtra_update_watch():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    cursor = conn.cursor()
    request_data = request.get_json()
    change_id = request_data['id']
    change_make = request_data['make']
    change_model = request_data['model']
    change_type = request_data['type']
    change_purchase_price = request_data['purchaseprice']
    change_sales_price = request_data['salesprice']
    sql = "UPDATE watches SET make=%s, model=%s, type=%s, purchaseprice=%s, salesprice=%s WHERE id=%s"
    data = (change_make, change_model, change_type, change_purchase_price, change_sales_price, change_id)
    cursor.execute(sql, data)
    conn.commit()
    sql = "SELECT * FROM watches"
    watches = execute_read_query(conn, sql)
    return jsonify(watches)


# POST
@app.route('/api/watch/xtra', methods=['POST'])
def xtra_add_watch():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    cursor = conn.cursor()
    request_data = request.get_json()
    add_make = request_data['make']
    add_model = request_data['model']
    add_type = request_data['type']
    add_purchase_price = request_data['purchaseprice']
    add_sales_price = request_data['salesprice']
    sql = "INSERT INTO watches (make, model, type, purchaseprice, salesprice) VALUES (UUID_TO_BIN(UUID()), %s, %s, %s, %s, %s)"
    data = (add_make, add_model, add_type, add_purchase_price, add_sales_price)
    cursor.execute(sql, data)
    conn.commit()
    sql = "SELECT * FROM watches"
    watches = execute_read_query(conn, sql)
    return jsonify(watches)


# DELETE
@app.route('/api/watch/xtra/token/<token>', methods=['DELETE'])
def xtra_del_watch(token):
    for valid_token in valid_tokens:
        if token == valid_token:
            my_creds = creds.Creds()
            conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
            cursor = conn.cursor()
            request_data = request.get_json()
            del_id = request_data['id']
            sql = "DELETE FROM watches WHERE id=%s"
            data = (del_id,)
            cursor.execute(sql, data)
            conn.commit()
            sql = "SELECT * FROM watches1"
            watches = execute_read_query(conn, sql)
            return jsonify(watches)
    return 'INVALID ACCESS TOKEN'


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)

