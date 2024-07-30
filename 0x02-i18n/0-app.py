#!/usr/bin/env python3
"""Module which handles the web app logic and routes as well as
the internationalization and localization"""

from flask import Flask
from flask import render_template

app: Flask = Flask(__name__)


@app.route("/")
def index() -> str:
    """Homepage route for Holberton webpage"""
    return render_template("index.html")
