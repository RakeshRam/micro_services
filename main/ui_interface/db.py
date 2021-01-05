from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

db = SQLAlchemy()


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(60))
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    series = db.Column(db.String(60))
    team = db.Column(db.String(60))
    origin = db.Column(db.String(60))
    ability = db.Column(db.String(60))
    archenemy = db.Column(db.String(60))
    creator = db.Column(db.String(60))
    is_villan = db.Column(db.Boolean)

    def __repr__(self):
        return self.name

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    character_id = db.Column(db.Integer)

    UniqueConstraint('username', 'character_id', name='user_character_unique')

    def __repr__(self):
        return self.username
    