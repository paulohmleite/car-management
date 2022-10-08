from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Color, Model
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


cars = Blueprint("cars", __name__)

@login_required
@cars.route("/car-color/", methods=["GET", "POST"])
def car_color_page():

    if request.method == "GET":
        colors = Color.query.all()

        return render_template('colors.html', user=current_user, colors=colors)

    if request.method == "POST":
        color = request.form.get("color")

        if len(color) < 1:
            flash("Color is too short!", category="error")
        else:
            new_color = Color(color=color)
            db.session.add(new_color)
            db.session.commit()
            flash("Color registered!", category="success")

    return render_template('colors.html', user=current_user)

@login_required
@cars.route("/car-model/", methods=["GET", "POST"])
def car_model_page():

    if request.method == "GET":
        models = Model.query.all()

        return render_template('models.html', user=current_user, models=models)

    if request.method == "POST":
        model = request.form.get("model")

        if len(model) < 1:
            flash("Model is too short!", category="error")
        else:
            new_model = Model(model=model)
            db.session.add(new_model)
            db.session.commit()
            flash("Model registered!", category="success")

    return render_template('models.html', user=current_user)

@login_required
@cars.route("/car-ownership/", methods=["GET", "POST"])
def car_ownership():

    if request.method == "GET":
        models = Model.query.all()
        colors = Color.query.all()
        models = Model.query.all()

        return render_template(
            'car_ownership.html', 
            user=current_user, 
            models=models,
            colors=colors
        )

    if request.method == "POST":
        model = request.form.get("model")

        if len(model) < 1:
            flash("Model is too short!", category="error")
        else:
            new_model = Model(model=model)
            db.session.add(new_model)
            db.session.commit()
            flash("Model registered!", category="success")

    return render_template('car_ownership.html', user=current_user)

@login_required
@cars.route("/possible-sales/", methods=["GET", "POST"])
def possible_sales():

    if request.method == "GET":
        possible_sales = User.query.all()

        return render_template('models.html', user=current_user, possible_sales=possible_sales)

    if request.method == "POST":
        model = request.form.get("model")

        if len(model) < 1:
            flash("Model is too short!", category="error")
        else:
            new_model = Model(model=model)
            db.session.add(new_model)
            db.session.commit()
            flash("Model registered!", category="success")

    return render_template('models.html', user=current_user)
