#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import psycopg2
import urlparse
from flask import Flask, Response, send_file, abort, request

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
    cur.execute('select b.username, b.is_main, h.revision from bots b, (select max(revision) as revision from bots_history) h;')
    rows = cur.fetchall()
    bots = []
    revision = 0
    for row in rows:
        bot = {"username": row[0], "is_main": row[1]}
        bots.append(bot)
        revision = row[2]
    conn.close()
    return {"revision": revision, "items": bots};

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

def get_bots_changes(revision):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select username, action, revision as revision from bots_history where revision > %s' % revision)
    rows = cur.fetchall()

    new_revision = revision
    added_bots = []
    removed_bots = []
    updated_bots = []
    for row in rows:
        username = row[0]
        action = row[1]
        new_revision = max(new_revision, row[2])
        if action == 'add':
            added_bots.append(username)
        elif action == 'remove':
            removed_bots.append(username)
        elif action == 'update':
            updated_bots.append(username)

    new_bots = added_bots + updated_bots
    added_bots_details = []
    updated_bots_details = []

    if new_bots:
        cur.execute('select username, is_main from bots where username in %s',(tuple(added_bots + updated_bots), ))
        rows = cur.fetchall()
        for row in rows:
            details = {"username": row[0], "is_main": row[1]}
            if row[0] in added_bots:
                added_bots_details.append(details)
            else:
                updated_bots_details.append(details)

    conn.close()
    removed_bots_details = [{"username": bot} for bot in removed_bots]
    return {
        "revision": new_revision,
        "removed": removed_bots_details,
        "added": added_bots_details,
        "updated": updated_bots_details
    }

@app.route('/bots')
def bots():
    revision = request.args.get('revision')
    if revision is None or revision == '':
        resp_dict = get_bots()
        return make_json_response(resp_dict)
    else:
        return make_json_response(get_bots_changes(revision))

@app.route('/chants')
def chants():
    resp_dict = {"items": get_chants()}
    return make_json_response(resp_dict)

if __name__ == '__main__':
    app.run(debug=True) #FIXME: remove debug
