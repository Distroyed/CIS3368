import flask
from flask import jsonify
from flask import request
from sql import create_connection
from sql import execute_read_query
import creds


############
# MYSQL CODE
############

# SQL COMMANDS to create table
# create table gem (
# id int,
# gemtype varchar(255),
# gemcolor varchar(255),
# price double
# );

# insert into gem (gemtype, gemcolor, carat, price)
# values ('diamond', 'clear', 24, 2000.12),
# ('ruby', 'red', 12, 757.39),
# ('opal', 'greenish-blue', 18, 245.00),
# ('sapphire', 'blue', 24, 3450.99)
# ('amethyst', 'purple', 18, 2500.99);

###########
# APIs
###########

