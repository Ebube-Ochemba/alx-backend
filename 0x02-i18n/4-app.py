#!/usr/bin/env python3
"""Entry point of the web application"""
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale() -> str:
    """Determine the best match with our supported languages."""
    # Check for 'locale' parameter in the request
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Use default behavior if no valid 'locale' parameter is found
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def index() -> Any:
    """renders a simple template"""
    return render_template("4-index.html", locale_selector=get_locale)


if __name__ == "__main__":
    app.run()
