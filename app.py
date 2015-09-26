#! /usr/bin/env python

import json
import os.path
from flask import Flask, Response, send_file, abort
app = Flask(__name__)

BOTS_COUNT=20
CHANTS_COUNT=20
BACKEND_URL="http://fenegram.herokuapp.com"

@app.route('/')
def index():
    return '''
    Welcome to Fenegram backend!
    <br/>
    Available methods:
    <br/>
    <a href="/ping">/ping</a>
    <br/>
    <a href="/bots">/bots</a>
    <br/>
    <a href="/chants">/chants</a>
    '''

@app.route('/ping')
def ping():
    return 'pong'

def create_bot(ind):
    return {
        "usernamename": "@fenegram_%s_bot" % ind, 
        "title": "Fenegram Bot %s" % ind, 
        "id": "bot_id_%s" % ind, 
        "image": "%s/static/icon%s.png" % (BACKEND_URL, ind),
        "description": "Bot Description %s" % ind
    }

def get_bots():
    return [create_bot(i) for i in xrange(1, BOTS_COUNT+1)]

@app.route('/bots')
def bots():
    resp_dict = {"items": get_bots()}
    return Response(json.dumps(resp_dict), mimetype='application/json')

def create_chant(ind):
    return {
        "title": "Fenerbahce chant %s" % ind,
        "lyrics": "Lorem ipsum",
        "url": "%s/static/chant%s.mp3" % (BACKEND_URL, ind)
    }

def get_chants():
    return [create_chant(i) for i in xrange(1, CHANTS_COUNT+1)]

@app.route('/chants')
def chants():
    resp_dict = {"items": get_chants()}
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
