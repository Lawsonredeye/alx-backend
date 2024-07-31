#!/usr/bin/env python3
"""Module which handles the web app logic and routes as well as
the internationalization and localization"""

from babel import default_locale
from flask import Flask, request
from flask import render_template
from flask_babel import Babel
from flask_babel import gettext
from flask_babel import _
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


home_title = gettext("test_title")
home_header = gettext("home_header")


@app.route("/", strict_slashes=False)
def index() -> str:
    """Homepage route for Holberton webpage"""
    return render_template("3-index.html", home_title =home_title, home_header=home_header)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
