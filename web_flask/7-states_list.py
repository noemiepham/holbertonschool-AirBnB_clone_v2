#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""

from flask import Flask, render_template
import models

app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(exception):
    """handle teardown"""
    models.storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """return all database in the db"""
    state = models.storage.all(models.State).values()
    return render_template('7-states_list.html', state=state)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port='5000')
