#!/usr/bin/python3
"""Script that starts a Flask application"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    """Remove current SQLAlchemy session"""
    storage.close()


@app.route('/states_list')
def states_list():
    """Enables '/states_list' route"""
    return render_template('7-states_list.html',
                           states=storage.all(State).values())


if __name__ == "__main__":
    app.run()
