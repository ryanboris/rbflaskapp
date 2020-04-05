from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import environ as ENV_VAR

app = Flask(__name__)
app.config.from_object(ENV_VAR['APP_SETTINGS'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(128))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f'<id {self.id}>'

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }


@app.route('/')
def index():
    return "hello!"


if __name__ == '__main__':
    app.run()
