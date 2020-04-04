import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def index():
    return 'Hello!'


@app.route('/<name>')
def hello_name(name):
    return f'Hello, {name}!'


if __name__ == '__main__':
    print(os.environ['APP_SETTINGS'])
    app.run()
