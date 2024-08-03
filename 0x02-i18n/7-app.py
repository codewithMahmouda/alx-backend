#!/usr/bin/env python3

"""
This module contains a user login system
"""
import pytz.exceptions
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from typing import Dict, Union

users: Dict = {
    1:
        {"name": "Balou",
         "locale": "fr",
         "timezone": "Europe/Paris"},
    2:
        {"name": "Beyonce",
         "locale": "en",
         "timezone": "US/Central"},
    3:
        {"name": "Spock",
         "locale": "kg",
         "timezone": "Vulcan"},
    4:
        {"name": "Teletubby",
         "locale": None,
         "timezone": "Europe/London"},
}


class Config(object):
    """Config class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Union[Dict, None]:
    """
    Return a user dictionary or None if the id
    couldn't be found
    """
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """"RUns Before request"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Translates to the best match language"""
    locale: str = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

    if g.user and 'locale' in g.user:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    header_locale: str = request.headers.get("locale")
    if header_locale:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    local_timezone = request.args.get("timezone")
    if local_timezone:
        try:
            timezone = pytz.timezone(local_timezone)
            print(f"Using local timezone: {timezone.zone}")
            return timezone.zone
        except pytz.exceptions.UnknownTimeZoneError:
            print("Unknown local timezone")
            return app.config["BABEL_DEFAULT_TIMEZONE"]

    if "timezone" in g.user:
        user_timezone = g.user["timezone"]
        try:
            timezone = pytz.timezone(user_timezone)
            print(f"Using user's timezone: {timezone.zone}")
            return timezone.zone
        except pytz.exceptions.UnknownTimeZoneError:
            print("Unknown user's timezone")
            return app.config["BABEL_DEFAULT_TIMEZONE"]

    print("Using default timezone")
    return app.config["BABEL_DEFAULT_TIMEZONE"]

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Index route for the flask app
    Returns:
            The translated text
    """
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(debug=True)
