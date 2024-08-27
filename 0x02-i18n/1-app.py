#!/usr/bin/env python3
"""Entry point of the web application"""
from flask import Flask, render_template
from flask_babel import Babel
from typing import Any

app = Flask(__name__)


class Config:
    """Configuration class for Babel"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# setup config for app
app.config.from_object(Config)

# Instantiate Babel
babel = Babel(app)


@app.route("/", strict_slashes=False)
def index() -> Any:
    """renders a simple template"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
