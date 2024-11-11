#!/usr/bin/env python3
"""Hello Holberton Flask Module task 3"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config class for task 1"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object('3-app.Config')
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Chooses the best match with supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=['GET'], strict_slashes=False)
def home() -> str:
    """ Define the route for home
        Return 3-index.html
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
