import os

from flask import Flask
from loguru import logger

app = Flask(__name__)

# Mock DB access, assert get DB credentials from k8s secrets.
username = os.environ['username']
password = os.environ['password']
if username == 'bo' and 'randompassword' in password:
    logger.info('db connection succeed!')
else:
    raise ValueError('Unable to read k8s secrets!')

# Read config from k8s configmap, other use default value for docker build without k8s
debug = os.environ.get('debug', True)
host = os.environ.get('host', '0.0.0.0')
port = os.environ.get('port', 5000)


@app.route('/')
def hello():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=debug, host=host, port=port)
