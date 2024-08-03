#!/usr/bin/env python3

"""
contains a Flask app and a route
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Index route for the flask app
    return:
            renders the 0-index.html file
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
