#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def List_of_states():
    """print simple string"""
    query_state = storage.all(State).values()
    query_citys = storage.all(City).values()

    return render_template("8-cities_by_states.html", data=query_state, data2=query_citys)


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
