#!/usr/bin/env python3
"""Hello Holberton Flask Module"""

from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """Config class for task 1"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object('1-app.Config')
babel = Babel(app)


@app.route("/", methods=['GET'], strict_slashes=False)
def home() -> str:
    """ Define the route for home
        Return 1-index.html
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
