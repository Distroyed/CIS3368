import flask
from flask import jsonify
from flask import request


# setting up an application name
app = flask.Flask(__name__)  # sets up the application
app.config["DEBUG"] = True  # allow to show errors in browser

cars = [
    {'id': 0,
     'make': 'Jeep',
     'model': 'Grand Cherokee',
     'year': 2000,
     'color': 'black'},
    {'id': 1,
     'make': 'Ford',
     'model': 'Mustang',
     'year': 1970,
     'color': 'white'},
    {'id': 2,
     'make': 'Dodge',
     'model': 'Challenger',
     'year': 2020,
     'color': 'red'
     }
]


# default url with any routing as a GET request
@app.route('/', methods=['GET'])
def home():
    return "<h1> WELCOME TO OUR FIRST API! </h1>"


# endpoint to get all cars
@app.route('/api/car/all', methods=['GET'])
def api_all():
    return jsonify(cars)


# endpoint to get a single car
@app.route('/api/car', methods=['GET'])
def api_id():
    if 'id' in request.args:  # only if an id is provided as an argument proceed
        id = int(request.args['id'])
    else:
        return 'ERROR: No ID provided!'
    results = []  # resulting car(s) to return
    for car in cars:
        if car['id'] == id:
            results.append(car)
    return jsonify(results)


# endpoint that will add a car as POST
@app.route('/api/car', methods=['POST'])
def add_car():
    request_data = request.get_json()
    newid = request_data['id']
    newmake = request_data['make']
    newmodel = request_data['model']
    newyear = request_data['year']
    newcolor = request_data['color']

    cars.append(
        {
            'id': newid,
            'make': newmake,
            'model': newmodel,
            'year': newyear,
            'color': newcolor
        }
    )

    return "Add request successful!"


@app.route('/api/car', methods=['DELETE'])
def del_car():
    request_data = request.get_json()
    id_to_delete = request_data['id']
    for i in range(len(cars)-1, -1, -1):  # start, stop, step size
        if cars[i]['id'] == id_to_delete:
            del(cars[i])

    return "Delete request successful"


@app.route('/api/users', methods=['GET'])
def api_users_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'ERROR: No ID provided!'
    my_creds = creds.Creds()
    conn = create_connection(my_creds.conString, my_creds.userName, my_creds.password, my_creds.dbName)
    sql = "SELECT * FROM users"
    users = execute_read_query(conn, sql)
    results = []

    for user in users:
        if user['id'] == id:
            results.append(user)

    return jsonify(results)

app.run()
