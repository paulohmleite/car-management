from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Color
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


cars = Blueprint("cars", __name__)

@login_required
@cars.route("/car-color/", methods=["GET", "POST"])
def car_color_page():

    if request.method == "POST":
        color = request.form.get("color")

        if len(color) < 1:
            flash("Color is too short!", category="error")
        else:
            new_color = Color(color=color)
            db.session.add(new_color)
            db.dession.commit()
            flash("Color registered!", category="success")

    return render_template('colors.html', user=current_user)

@login_required
@cars.route("/car-model/", methods=["GET", "POST"])
def car_model_page():

    if request.method == "POST":
        model = request.form.get("model")

        if len(model) < 1:
            flash("Model is too short!", category="error")
        else:
            new_color = Color(color=model)
            db.session.add(new_color)
            db.dession.commit()
            flash("Model registered!", category="success")

    return render_template('models.html', user=current_user)