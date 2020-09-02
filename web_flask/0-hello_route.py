#!/usr/bin/python3
"""Script that starts a Flask application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Function that generates the route"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run()
