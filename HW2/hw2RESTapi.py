############
# MYSQL CODE
############

# SQL COMMANDS to create table
# create table gem (
# id int NOT NULL auto_increment,
# gemtype varchar(255) NOT NULL,
# gemcolor varchar(255) NOT NULL,
# carat smallint NOT NULL,
# price double  NOT NULL,
# PRIMARY KEY (id)
# );

# insert into gem (gemtype, gemcolor, carat, price)
# values ('diamond', 'clear', 24, 2000.12),
# ('ruby', 'red', 12, 757.39),
# ('opal', 'greenish-blue', 18, 245.00),
# ('sapphire', 'blue', 24, 3450.99),
# ('amethyst', 'purple', 18, 2500.99);

import flask
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


@app.route('/', methods=['GET'])
def home():
    return "<h1> If you see this, they will grade </h1>"


# GET
@app.route('/api/gem', methods=['GET'])
def gem_all():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    sql = "SELECT * FROM gem"
    gems = execute_read_query(conn, sql)
    return jsonify(gems)


# PUT
@app.route('/api/gem', methods=['PUT'])
def update_gem():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    cursor = conn.cursor()
    request_data = request.get_json()
    change_id = request_data['id']
    change_gem_type = request_data['gemtype']
    change_gem_color = request_data['gemcolor']
    change_carat = request_data['carat']
    change_price = request_data['price']
    sql = "UPDATE gem SET gemtype=%s, gemcolor=%s, carat=%s, price=%s WHERE id=%s"
    data = (change_gem_type, change_gem_color, change_carat, change_price, change_id)
    cursor.execute(sql, data)
    conn.commit()
    sql = "SELECT * FROM gem"
    gems = execute_read_query(conn, sql)
    return jsonify(gems)


# POST
@app.route('/api/gem', methods=['POST'])
def add_gem():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    cursor = conn.cursor()
    request_data = request.get_json()
    new_gem_type = request_data['gemtype']
    new_gem_color = request_data['gemcolor']
    new_carat = request_data['carat']
    new_price = request_data['price']
    sql = "INSERT INTO gem (gemtype, gemcolor, carat, price) VALUES (%s, %s, %s, %s)"
    data = (new_gem_type, new_gem_color, new_carat, new_price)
    cursor.execute(sql, data)
    conn.commit()
    sql = "SELECT * FROM gem"
    gems = execute_read_query(conn, sql)
    return jsonify(gems)


# DELETE
@app.route('/api/gem', methods=['DELETE'])
def del_gem():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    cursor = conn.cursor()
    request_data = request.get_json()
    del_id = request_data['id']
    sql = "DELETE FROM gem WHERE id = %s;"
    data = del_id
    cursor.execute = (sql, data)
    conn.commit()
    sql = "SELECT * FROM gem"
    gems = execute_read_query(conn, sql)
    return jsonify(gems)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)



