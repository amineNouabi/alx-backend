#!/usr/bin/env python3
"""

Flask app

"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def root():
    """Root route"""
    return render_template("0-index.html")


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
