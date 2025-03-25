#!/usr/bin/env python

#-----------------------------------------------------------------------
# route_test.py
# Author: Andres Blanco Bonilla
#-----------------------------------------------------------------------

import flask

#-----------------------------------------------------------------------

app = flask.Flask(__name__, template_folder='.')

#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/route', methods=['GET'])
def route():

    html_code = flask.render_template('route_test.html')
    response = flask.make_response(html_code)
    return response

@app.route('/nj', methods=['GET'])
def nj_map():

    html_code = flask.render_template('nj_map.html')
    response = flask.make_response(html_code)
    return response