#! /usr/bin/env python

import json
from flask import Flask, Response
app = Flask(__name__)

@app.route('/ping')
def index():
    return 'pong'

def create_bot(ind):
    return {
        "name": "fenegram_bot %s" % ind, 
        "image": "http://fenegram-bot-store.herokuapp.com/icon%s.jpg" % ind,
        "description": "Bot Description %s" % ind
    }

def get_bots():
    return [create_bot(i) for i in xrange(1,21)]

@app.route('/list')
def list():
    resp_dict = {"items": get_bots()}
    return Response(json.dumps(resp_dict), mimetype='application/json')

if __name__ == '__main__':
    app.run()
