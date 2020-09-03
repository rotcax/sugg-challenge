from flask import Flask
from .constants import ENVIRONMENT

app = Flask(__name__)
app.env = ENVIRONMENT

@app.errorhandler(404)
def endpoint_not_found(error):
    return { 'result': 'not_found' }, 404

@app.route('/')
def principal_endpoint():
    return { 'result': 'Welcome to challenge, please try one request with post method' }, 200
