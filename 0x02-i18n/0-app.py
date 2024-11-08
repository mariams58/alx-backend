#!/usr/bin/env python3
"""Hello Holberton Flask Module"""

from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    """ Define the route for home"""
    return render_template("templates/0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
