#! /usr/bin/env python

import json
import os.path
from flask import Flask, Response, send_file, abort
app = Flask(__name__)


@app.route('/')
def index():
    return 'Available methods:\n/ping\n/list'

@app.route('/ping')
def ping():
    return 'pong'

def create_bot(ind):
    return {
        "usernamename": "@fenegram_%s_bot" % ind, 
        "title": "Fenegram Bot %s" % ind, 
        "id": "bot_id_%s" % ind, 
        "image": "http://fenegram-bot-store.herokuapp.com/static/icon%s.png" % ind,
        "description": "Bot Description %s" % ind
    }

def get_bots():
    return [create_bot(i) for i in xrange(1,21)]

@app.route('/list')
def list():
    resp_dict = {"items": get_bots()}
    return Response(json.dumps(resp_dict), mimetype='application/json')

@app.route('/static/<string:filename>')
def static_file(filename):
    path = "static/" + filename
    if os.path.isfile(path):
        return send_file(path)
    else:
        abort(404)


if __name__ == '__main__':
    app.run()
