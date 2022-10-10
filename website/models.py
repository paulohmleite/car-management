from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

import flask_sqlalchemy

# db = flask_sqlalchemy.SQLAlchemy()


class Color(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(20))

    def get_all(model):
        data = model.query.all()
        return data

    def add_instance(model, **kwargs):
        instance = model(**kwargs)
        db.session.add(instance)
        db.session.commit_changes()

    def delete_instance(model, id):
        model.query.filter_by(id=id).delete()
        db.session.commit_changes()
    
    def edit_instance(model, id, **kwargs):
        instance = model.query.filter_by(id=id).all()[0]
        for attr, new_value in kwargs.items():
            setattr(instance, attr, new_value)
        db.session.commit_changes()


class Model(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(20))


class Car(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    color_id = db.Column(db.Integer, db.ForeignKey("color.id"))
    model_id = db.Column(db.Integer, db.ForeignKey("model.id"))


class User(db.Model, UserMixin):
    id         = db.Column(db.Integer, primary_key=True)
    email      = db.Column(db.String(150), unique=True)
    password   = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name  = db.Column(db.String(150))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    is_staff   = db.Column(db.Boolean, default=False, nullable=False)
    is_admin   = db.Column(db.Boolean, default=False, nullable=False)
    cars       = db.relationship("Car")

    # business rules
    # one user can have a maximum of three cars.
