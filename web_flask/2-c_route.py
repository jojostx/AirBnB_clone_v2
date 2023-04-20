#!/usr/bin/python3
""" script that runs an app with Flask framework """
from flask import Flask, request


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """ Function called with / route """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function called with /hbnb route """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Function called with /c/<text> route """
    return 'C %s' % text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
