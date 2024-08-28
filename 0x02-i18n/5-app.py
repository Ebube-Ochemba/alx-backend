#!/usr/bin/env python3
"""Entry point of the web application"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Any, Dict, Union

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

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """Determine the best match with our supported languages."""
    # Check for 'locale' parameter in the request
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    # Use default behavior if no valid 'locale' parameter is found
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user() -> Union[Dict, None]:
    """Retrieve a user by provided id."""
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request() -> None:
    """Set the user as a global variable on flask.g"""
    g.user = get_user()


@app.route("/", strict_slashes=False)
def index() -> Any:
    """renders a simple template"""
    return render_template("5-index.html", locale_selector=get_locale)


if __name__ == "__main__":
    app.run()
