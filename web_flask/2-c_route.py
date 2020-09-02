#!/usr/bin/python3
"""Script that starts a Flask application with:
'/' route
'/hbnb' route
'/c/<text>' route"""

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


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Function that enables '/c/<text>' route"""
    return 'C {}'.format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()
