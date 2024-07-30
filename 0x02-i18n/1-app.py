#!/usr/bin/env python3
"""Module which handles the web app logic and routes as well as
the internationalization and localization"""

from pickle import FALSE
from babel import default_locale
from flask import Flask
from flask import render_template
from flask_babel import Babel
from pytz import UTC

app: Flask = Flask(__name__)


class Config:
    """Config settings for flask instance"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = UTC


app.config.from_object(Config)

babel = Babel(app)


@app.route("/", strict_slashes=False)
def index() -> str:
    """Homepage route for Holberton webpage"""
    return render_template("index.html")
