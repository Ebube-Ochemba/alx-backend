#!/usr/bin/python3
"""Entry point of the web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """renders a simple template """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
