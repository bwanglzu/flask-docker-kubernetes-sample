import os

from flask import Flask
from loguru import logger

app = Flask(__name__)

# Read config from k8s configmap.
host = os.environ['host']
port = os.environ['port']
debug = os.environ['debug']

# Mock DB access, assert get DB credentials from k8s secrets.
username = os.environ['username']
password = os.environ['password']
if username and password:
    logger.info('db connection succeed!')
else:
    raise ValueError('Unable to read k8s secrets!')

@app.route('/')
def hello():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=debug, host=host, port=port)
