from unicodedata import category
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Car
from . import db

views = Blueprint("views", __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        car = request.form.get("car")

        if len(car) < 1:
            flash("Car is too short!", category="error")
        else:
            new_car = Car(owner_id=current_user.id)
            db.session.add(new_car)
            db.dession.commit()
            flash("Car registered!", category="success")

    return render_template("home.html", user=current_user)


@login_required
@views.route('/adm/')
def adm():
    return render_template("adm.html", user=current_user)

