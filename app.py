from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello!'


@app.route('/<name>')
def hello_name(name):
    return f'Hello, {name}!'


if __name__ == '__main__':
    app.run()
