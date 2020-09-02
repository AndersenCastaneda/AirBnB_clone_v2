#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """Displays a HTML page whit state list"""
    states = list(storage.all(State).values())
    return render_template('7-states_list', states=states)


@app.teardown_appcontext
def close_session(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
