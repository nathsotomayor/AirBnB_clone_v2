#!/usr/bin/python3
"""Script that starts a Flask application
main route ('/') and '/hbnb' route"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Function that generates the main route"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function that enables '/hbnb' route"""
    return 'HBNB'


if __name__ == "__main__":
    app.run()
