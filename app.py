import os

from dotenv import load_dotenv
from flask import Flask


load_dotenv()


__version__ = os.environ['VERSION']


app = Flask(__name__)


@app.route('/')
def hello_world():
    return f'Hello, World! v{__version__}'
