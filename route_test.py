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
def index():

    html_code = flask.render_template('route_test.html')
    response = flask.make_response(html_code)
    return response