#!/usr/bin/python3
"""
Script that starts a Flask web application
and print in two different routes
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def main_route():
    """print simple string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def second_route():
    """print simple string"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def third_route(text):
    """ display “C ” followed by the value= text"""
    text = text.replace("_", " ")
    return "C {}".format(escape(text))


@app.route("/python/<text>", strict_slashes=False)
def fourth_route(text="is cool"):
    """ display “C ” followed by the value= text"""
    text = text.replace("_", " ")
    return "Python {}".format(escape(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
