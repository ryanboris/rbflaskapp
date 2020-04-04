from app import db


class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(128))

    def __repr__(self):
        return f'<id {self.id}>'
