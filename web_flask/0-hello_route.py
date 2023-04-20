#!/usr/bin/python3
""" script that runs an app with Flask framework """
from flask import Flask, request


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """ Function called with / route """
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
