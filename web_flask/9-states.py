#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def List_of_states():
    """print simple string"""
    query_state = storage.all(State).values()

    return render_template("9-states.html", data=query_state)


@app.route("/states/<id>", strict_slashes=False)
def List_of_states_and_citys(id):
    """print simple string"""
    query_state = storage.all(State).values()
    query_citys = storage.all(City).values()

    found = 0

    for state in query_state:
        if id == state.id:
            found = 1

    return render_template("9-states.html", data=query_state,
                           data2=query_citys, id=id, found=found)


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
