from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(20))


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(20))


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    color_id = db.Column(db.Integer, db.ForeignKey("color.id"))
    model_id = db.Column(db.Integer, db.ForeignKey("model.id"))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    cars = db.relationship("Car")

    # business rules
    # one user can have a maximum of three cars.
