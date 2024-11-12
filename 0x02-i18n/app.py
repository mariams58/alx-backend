#!/usr/bin/env python3
"""Hello Holberton Flask Module task 3"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone, exceptions, utc
frome datetime import datetime
import locale


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config class for task 1"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object('3-app.Config')
babel = Babel(app)


def get_user() -> dict:
    """ Resturns a mock data if user is valid or None """
    idx: str = request.args.get('login_as')
    if idx:
        return users.get(int(idx))
    return None


@app.before_request
def before_request() -> None:
    """ Set a global user if valid in mockdb """
    user: dict = get_user()
    if user:
        g.user: g = user
    tze = timezone(get_timezone())
    c_time: datetime = tze.localize(datetime.utcnow())
    txt: str = "%b %d %Y %I:%M:%S %p"
    g.current_time: datetime = c_time.strftime(fmt)


@babel.localeselector
def get_locale() -> str:
    """ Chooses the best match with supported languages"""
    lang: str = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    # get local from global user setting
    if g.user:
        lang = g.user.get('locale')
        if lang and lang in app.config['LANGUAGES']:
            return lang
    # get local from request header
    lang = request.headers.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """ Chooses the correct timezone for each location """
    tze: str = request.args.get('timezone')
    if tze:
        try:
            return timezone(tze).zone
        except exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        try:
            tze = g.user.get('timezone')
            return timezone(tze).zone
        except exceptions.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route("/", methods=['GET'], strict_slashes=False)
def home() -> str:
    """ Define the route for home
        Return index.html
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
