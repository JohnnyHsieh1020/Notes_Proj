# Create DB models
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    notes = db.relationship('Note')


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # F-key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
