#!/usr/bin/env python
import flask
import json

from flask import jsonify
from pydruid.client import *
from pydruid.utils.aggregators import longsum

# Create the application.
APP = flask.Flask(__name__)

# ***************************
#   START OF CODE CHANGES
#
#  Task: Fill in the value for 'DRUID_URL' below.
# ***************************

DRUID_URL = ''

# ***************************
#   END OF CODE CHANGES
# ***************************
DRUID_QUERY = PyDruid(DRUID_URL, 'druid/v2')

@APP.route('/')
def root():
    return 'Hello World!'

def run_query():
    # ***************************
    #   START OF CODE CHANGES
    #
    #  Task: Replace 'druid_query' with a pydruid query
    # ***************************
    
    druid_query = None
    
    # ***************************
    #   END OF CODE CHANGES
    # ***************************

    # Returns data in json format
    return json.loads(druid_query.result_json)

def transform_data(data):
    # *************************
    #   START OF CODE CHANGES
    #
    #  Task: Replace the statement below with code that converts the contents of
    #  'data' into the content you want your API endpoint to emit.
    # *************************
    
    return None
    
    # *************************
    #   END OF CODE CHANGES
    # *************************

@APP.route('/get_data')
def get_data(): 
    druid_data = run_query()
    response = jsonify(transform_data(druid_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    APP.debug=True
    # Since this is running on AWS, change host
    APP.run(host='0.0.0.0', port=5000)
