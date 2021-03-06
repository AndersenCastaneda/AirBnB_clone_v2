#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Response Hello HBNB! to a request"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Response HBNB to a request"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Response C <text> to a request"""
    text = text.replace('_', ' ')
    return 'C %s' % text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Response Python (<text>) to a request"""
    text = text.replace('_', ' ')
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def a_number(n):
    """Response <n> is a number to a request"""
    if type(n) == int:
        return '%s is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_number(n):
    """Response a HTML template to a request"""
    if type(n) == int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd(n):
    """Response a HTML template to a request"""
    if type(n) == int:
        if n % 2 == 0:
            msg = 'is even'
            return render_template('6-number_odd_or_even.html', n=n, msg=msg)
        else:
            msg = 'is odd'
            return render_template('6-number_odd_or_even.html', n=n, msg=msg)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
