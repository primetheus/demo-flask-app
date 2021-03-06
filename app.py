#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/hello/<username>')
def hello_user(username):
    return f'Why, hello {username}!\n'

if __name__ == '__main__':
    # Listen on all interfaces
    app.run(host='0.0.0.0')
