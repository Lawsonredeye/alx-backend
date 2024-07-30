#!/usr/bin/env python3
"""Module which handles the web app logic and routes as well as
the internationalization and localization"""

from flask import Flask
from flask import render_template

app: Flask = Flask(__name__)


@app.route("/", strict_slashes=False)
def index() -> str:
    """Homepage route for Holberton webpage"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
