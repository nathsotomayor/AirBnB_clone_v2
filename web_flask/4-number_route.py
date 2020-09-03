#!/usr/bin/python3
"""Script that starts a Flask application with:
'/' route
'/hbnb' route
'/c/<text>' route
'/python/<text>' route default text='is cool'
'/number/<n>' route"""

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


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """Function that enables '/python/<text>' route"""
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
    """Function that enables '/number/<n>' route"""
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run()
