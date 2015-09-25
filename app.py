#! /usr/bin/env python

import json
from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Fenegram Bots'

def create_bot(ind):
    return {
        "name": "fenegram_bot %s" % ind, 
        "image": "http://fenegram-bot-store.herokuapp.com/icon%s.jpg" % ind,
        "description": "Bot Description %s" % ind
    }

@app.route('/list')
def list():
    bots = [create_bot(i) for i in xrange(1,21)]
    resp_dict = {"items": bots}
    return Response(json.dumps(resp_dict), mimetype='application/json')

if __name__ == '__main__':
    app.run()
