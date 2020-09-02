#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """Displays a HTML page whit state_id list"""
    states = storage.all(State)
    if id is not None:
        key = '{}.{}' format(State, id)
        if key in states:
            states = states[key]
        else:
            states = None
    else:
        states = list(storage.all(State).values())
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
