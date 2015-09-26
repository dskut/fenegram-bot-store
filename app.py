#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import psycopg2
import urlparse
from flask import Flask, Response, send_file, abort

app = Flask(__name__)
urlparse.uses_netloc.append("postgres")
db_url = urlparse.urlparse(os.environ.get("DATABASE_URL", 'postgres://dskut:ded3893706@localhost/fenegram'))

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

def get_conn():
    return psycopg2.connect(
        database=db_url.path[1:],
        user=db_url.username,
        password=db_url.password,
        host=db_url.hostname,
        port=db_url.port
    )

def get_bots():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select username, is_main from bots;')
    rows = cur.fetchall()
    res = []
    for row in rows:
        chant = {"username": row[0], "is_main": row[1]}
        res.append(chant)
    conn.close()
    return res;

def make_json_response(d):
    text = json.dumps(d, ensure_ascii=False)
    return Response(text, mimetype='application/json; charset=utf-8')

def get_chants():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select title, lyrics, url from chants;')
    rows = cur.fetchall()
    res = []
    for row in rows:
        chant = {"title": row[0], "lyrics": row[1], "url": row[2]}
        res.append(chant)
    conn.close()
    return res

@app.route('/bots')
def bots():
    resp_dict = {"items": get_bots()}
    return make_json_response(resp_dict)

@app.route('/chants')
def chants():
    resp_dict = {"items": get_chants()}
    return make_json_response(resp_dict)

if __name__ == '__main__':
    app.run(debug=True) #FIXME: remove debug
