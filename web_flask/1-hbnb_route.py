#!/usr/bin/python3
"""
Script that starts a Flask web application
and print in two different routes
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def main_route():
    """print simple string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def second_route():
    """print simple string"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
