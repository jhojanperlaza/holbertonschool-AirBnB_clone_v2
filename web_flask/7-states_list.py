#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def List_of_states():
    """print simple string"""
    query_storage = storage.all(State).values()
    return render_template("7-states_list.html", data=query_storage)

@app.teardown_appcontext
def close(self):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
