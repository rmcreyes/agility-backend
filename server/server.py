"""Interface the flask app by mapping paths to functions."""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    """Return 'hello, world!' for this root route."""
    return 'Hello, world!'
