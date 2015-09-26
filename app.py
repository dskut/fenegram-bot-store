#! /usr/bin/env python
# -*- coding: utf-8 -*-

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

@app.route('/static/<string:filename>')
def static_file(filename):
    path = "static/" + filename
    if os.path.isfile(path):
        return send_file(path)
    else:
        abort(404)

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

def make_json_response(d):
    text = json.dumps(d, ensure_ascii=False)
    return Response(text, mimetype='application/json; charset=utf-8')

def create_chant(ind):
    return {
        "title": "Bir Tek Sana Tutuldu Bu Kalpler %s" % ind,
        "lyrics": '''Bir tek sana tutuldu bu kalpler
Sevdanın uğruna tanımaz hiç engel
Bizim için heves değilsin sen FENER
Aşkın bize yeter!''',
        "url": "%s/static/chant%s.mp3" % (BACKEND_URL, ind)
    }

def get_chants():
    return [create_chant(i) for i in xrange(1, CHANTS_COUNT+1)]

@app.route('/bots')
def bots():
    resp_dict = {"items": get_bots()}
    return make_json_response(resp_dict)

@app.route('/chants')
def chants():
    resp_dict = {"items": get_chants()}
    return make_json_response(resp_dict)

if __name__ == '__main__':
    app.run(debug=True)
