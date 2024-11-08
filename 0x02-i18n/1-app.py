#!/usr/bin/env python3
"""

Flask app

"""

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    App Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@app.route("/", strict_slashes=False)
def root():
    """Root route"""
    return render_template("1-index.html")


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
