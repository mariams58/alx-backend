#!/usr/bin/env python3
"""Hello Holberton Flask Module task 2"""

from flask import Flask, render_template, request
from flask_babel import Babel
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Chooses the best match with suppoted languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=['GET'], strict_slashes=False)
def home() -> str:
    """ Define the route for home
        Return 2-index.html
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
