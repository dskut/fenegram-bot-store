#! /usr/bin/env python

from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Fenegram Bots'

@app.route('/list')
def list():
    json = '{"items":[{"name": "fenegram_bot", "image": "http://fenegram-bot-store.herokuapp.com/icon.jpg", "description": "Fenerbahce Yandex bot"}]}'
    return Response(json, mimetype='application/json')

if __name__ == '__main__':
    app.run()
