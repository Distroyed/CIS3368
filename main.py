import flask
import datetime
import time
import hashlib
from flask import jsonify, request,make_response
from sql import create_connection, execute_read_query
import creds


app = flask.Flask(__name__)  # sets up the application
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1> If you see this, they will grade </h1>"

masterUserName = "jeremy"
masterPassword = "secret"

@app.route('/api/auth', methods=['GET'])
def login_auth():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    sql = "SELECT * FROM users"
    users = execute_read_query(conn, sql)
    return jsonify(users)

#################################
# Airport Table CRUD API
#################################


# GET AIRPORT TABLE
@app.route('/api/airport', methods=['GET'])
def airport_all():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    sql = "SELECT * FROM airport"
    airports = execute_read_query(conn, sql)
    return jsonify(airports)


# PUT AIRPORT TABLE
@app.route('/api/airport', methods=['PUT'])
def update_airport():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    cursor = conn.cursor()
    request_data = request.get_json()
    change_airport_code = request_data['airportcode']
    change_airport_name = request_data['airportname']
    change_country = request_data['country']
    sql = "UPDATE airport SET airportcode=%s, airportname=%s, country=%s WHERE airportcode=%s"
    data = (change_airport_code, change_airport_name, change_country, change_airport_code)
    cursor.execute(sql, data)
    conn.commit()
    airports = "SELECT * FROM airport"
    airports = execute_read_query(conn, sql)
    return jsonify(airports)

# POST AIRPORT TABLE
@app.route('/api/airport', methods=['POST'])
def add_airport():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    cursor = conn.cursor()
    request_data = request.get_json()
    add_airport_code = request_data['airportcode']
    add_airport_name = request_data['airportname']
    add_country = request_data['country']
    sql = "INSERT INTO airport (airportcode, airportname, country) VALUES (%s, %s, %s)"
    data = (add_airport_code, add_airport_name, add_country)
    cursor.execute(sql, data)
    conn.commit()
    sql = "SELECT * FROM airport"
    airports = execute_read_query(conn, sql)
    return jsonify(airports)

# DELETE AIRPORT TABLE
@app.route('/api/airport', methods=['DELETE'])
def del_airport():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    cursor = conn.cursor()
    request_data = request.get_json()
    del_airport_id = request_data['airportcode']
    sql = "DELETE FROM airport WHERE airportcode=%s"
    data = (del_airport_code,)
    cursor.execute(sql, data)
    conn.commit()
    sql = "SELECT * FROM airport"
    airports = execute_read_query(conn, sql)
    return jsonify(airports)


#################################
# Plane Table CRUD API
#################################


# GET PLANE TABLE
@app.route('/api/plane', methods=['GET'])
def plane_all():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    sql = "SELECT * FROM plane"
    planes = execute_read_query(conn, sql)
    return jsonify(planes)


# PUT PLANE TABLE
@app.route('/api/plane', methods=['PUT'])
def update_plane():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    cursor = conn.cursor()
    request_data = request.get_json()
    change_make = request_data['make']
    change_model = request_data['model']
    change_year = request_data['year']
    change_capacity = request_data['capacity']
    sql = "UPDATE plane SET make=%s, model=%s, year=%s, capacity=%s WHERE planeid=%s"
    data = (change_make, change_model, change_year, change_capacity, change_plane_id)
    cursor.execute(sql, data)
    conn.commit()
    sql = "SELECT * FROM airport"
    planes = execute_read_query(conn, sql)
    return jsonify(planes)


# POST PLANE TABLE
@app.route('/api/plane', methods=['POST'])
def add_plane():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    cursor = conn.cursor()
    request_data = request.get_json()
    add_make = request_data['make']
    add_model = request_data['model']
    add_year = request_data['year']
    add_capacity = request_data['capacity']
    sql = "INSERT INTO plane (make, model, year, capacity) VALUES (%s, %s, %s, %s)"
    data = (add_make, add_model, add_year, add_capacity)
    cursor.execute(sql, data)
    conn.commit()
    sql = "SELECT * FROM plane"
    planes = execute_read_query(conn, sql)
    return jsonify(planes)


# DELETE AIRPORT TABLE
@app.route('/api/plane', methods=['DELETE'])
def del_plane():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    cursor = conn.cursor()
    request_data = request.get_json()
    del_make = request_data['make']
    del_model = request_data['model']
    del_year = request_data['year']
    sql = "DELETE FROM plane WHERE year=%s AND make=%s AND model=%s"
    data = (del_year, del_make, del_model)
    cursor.execute(sql, data)
    conn.commit()
    sql = "SELECT * FROM plane"
    planes = execute_read_query(conn, sql)
    return jsonify(planes)

#################################
# Flight Table CRUD API
#################################


# GET FLIGHT TABLE
@app.route('/api/flight', methods=['GET'])
def flight_all():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    sql = "SELECT date, departureairport.airportname AS 'DepartingAirport', arrivalairport.airportname AS 'ArrivalAirport', plane.make, plane.model, plane.capacity from flight INNER JOIN airport as departureairport ON flight.airportfromid=departureairport.airportid INNER JOIN airport as arrivalairport ON flight.airporttoid=arrivalairport.airportid JOIN plane ON plane.planeid=flight.planeid"
    flights = execute_read_query(conn, sql)
    return jsonify(flights)

# POST FLIGHT TABLE
@app.route('/api/flight', methods=['POST'])
def add_flight():
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    cursor = conn.cursor()
    request_data = request.get_json()
    add_plane_id = request_data['planeid']
    add_airport_from_id = request_data['airportfromid']
    add_airport_to_id = request_data['airporttoid']
    add_date = request_data['date']
    sql = "INSERT INTO flight (make, model, year, capacity) VALUES (%s, %s, %s, %s)"
    data = (add_plane_id, add_airport_from_id, add_airport_to_id, add_date)
    cursor.execute(sql, data)
    conn.commit()
    sql = "SELECT * FROM flight"
    flights = execute_read_query(conn, sql)
    return jsonify(flights)


app.run()