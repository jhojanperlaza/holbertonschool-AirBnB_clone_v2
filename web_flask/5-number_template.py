#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
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


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def fourth_route(text):
    """ display “Python ”, followed by the value of the text"""
    text = text.replace("_", " ")
    return "Python {}".format(escape(text))


@app.route("/number/<int:n>", strict_slashes=False)
def five_route(n):
    """ display “n is a number” only if n is an integer"""
    return "{} is a number".format(escape(n))

@app.route("/number_template/<int:n>", strict_slashes=False)
def six_route(n):
    """ display a HTML page only if n is an integer"""
    return render_template('5-number.html', data=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
