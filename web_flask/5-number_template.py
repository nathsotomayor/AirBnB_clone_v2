#!/usr/bin/python3
"""Script that starts a Flask application with:
'/' route
'/hbnb' route
'/c/<text>' route
'/python/<text>' route default text='is cool'
'/number/<n>' route"""

from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """Function that generates the main route"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Function that enables '/hbnb' route"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Function that enables '/c/<text>' route"""
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_is_cool(text):
    """Function that enables '/python/<text>' route"""
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>')
def is_num(n):
    """Function that enables '/number/<n>' route"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def num_template(n):
    """Function that enables '/number_template/<n>' route"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run()
