#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models.city import City
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_cities():
    """Displays a HTML page whit state list"""
    states = list(storage.all(State).values())
    cities = list(storage.all(City).values())
    return render_template('8-cities_by_states.html', states=states, cities=cities)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
