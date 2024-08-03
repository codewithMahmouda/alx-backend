#!/usr/bin/env python3

"""Contains a flask app and a babel class"""

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """Config class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Index route for the flask app
    Return:
            Renders the 1-index.html file
            English as the default locale
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
