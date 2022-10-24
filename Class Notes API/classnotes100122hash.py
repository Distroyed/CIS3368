import hashlib
import datetime
import time
import flask
from flask import jsonify
from flask import request, make_response

# 5316911983139663491615228241121400000 GUID/UUID
# 80658175170943878571660636856403766975289505440883277824000000000000 = 52!
# 115792089237316195423570985008687907853269984665640564039457584007913129639936 = 2^256, SHA256


# setting up an application name
app = flask.Flask(__name__)  # sets up the application
app.config["DEBUG"] = True  # allow to show errors in browser

# password 'password' hashed
master_password = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
master_name = 'username'
valid_tokens = {
    '100', '200', '300', '400'
}


# basic http authentication, prompts username and password upon contacting the endpoint
@app.route('/authenticatedroute', methods=['GET'])
def auth_example():
    if request.authorization:
        encoded = request.authorization.password.encode()  # unicode encoding
        hashed_result = hashlib.sha256(encoded)
        if request.authorization.username == master_name and hashed_result.hexdigest() == master_password:
            return '<h1> WE ARE ALLOWED TO BE HERE! </h1>'
    return make_response('COULD NOT VERIFY!', 401, {'WWW-Authenticate': 'Basic realm = "Login Required"'})


# token submission as part of the url, similar to how personal tokens are part of SMS auth.
@app.route('/api/token/<token>', methods=['GET'])
def auth_token(token):
    for valid_token in valid_tokens:
        if token == valid_token:  # check if token is valid, compared against a set of valid token in a db table
            return '<h1> CONGRATULATIONS, AUTH Successful </h1>'
    return 'INVALID ACCESS TOKEN'


# tokens that have an expiration dat and time, is given if the token is not expired
# for instance, time token valid until Jan 1, 2030 (still valid): 1893456000
# for instance, time token valid until Jan 2, 2020 (no longer valid): 1640995200
# date = datetime.datetime(2022,1,1)
@app.route('/api/timetoken/<timetoken>', methods=['GET'])
def auth_timetoken(timetoken):
    if float(timetoken) > time.time():  # checks if the token is greater than current date
        return '<h1> YOUR TIME TOKEN IS VALID </h1>'
    return '<h1> YOUR TIME TOKEN HAS EXPIRED</h1>'


authorized_users = [
    {
        'username': 'username',
        'password': 'password',
        'role': 'default',
        'token': '0',
        'admininfo': None
    },
    {
        'username': 'jeremy',
        'password': 'admin',
        'role': 'admin',
        'token': '1234567890',
        'admininfo': 'something applicable to admin'
    }
]


# route to auth with username and password against a dataset (ideally from DB w/ password hashed)
@app.route('/api/usernamepw', methods=['GET'])
def usernamepw_auth():
    username = request.headers['username']  # get the header parameters (as dictionaries)
    password = request.headers['password']
    for au in authorized_users:
        if au['username'] == username and au['password'] == password:
            session_token = au['token']
            admin_info = au['admininfo']
            returninfo = []
            returninfo.append(au['role'])
            returninfo.append(session_token)
            returninfo.append(admin_info)
            return jsonify(returninfo)
    return 'SECURITY ERROR'  # never give details on what went wrong


app.run()
