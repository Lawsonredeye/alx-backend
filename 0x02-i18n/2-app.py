#!/usr/bin/env python3
"""Module which handles the web app logic and routes as well as
the internationalization and localization"""

from babel import default_locale
from flask import Flask, request
from flask import render_template
from flask_babel import Babel
from pytz import UTC

app: Flask = Flask(__name__)


class Config:
    """Config settings for flask instance"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """returns the best match based of the client and specificity"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index() -> str:
    """Homepage route for Holberton webpage"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
