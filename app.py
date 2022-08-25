#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1> Final Site Tata!!!</h1>'

app.run(host='0.0.0.0',port=5000)
