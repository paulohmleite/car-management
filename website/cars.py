from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from .models import User, Color, Model, Car
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import json


cars = Blueprint("cars", __name__)

@login_required
@cars.route("/car-color/", methods=["GET", "POST"])
def car_color_page():

    # if request.user.

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

    return redirect(url_for('cars.car_color_page'))

@cars.route('/delete-color', methods=['POST'])
def delete_note():
    color = json.loads(request.data)
    colorId = color['colorId']
    color = Color.query.get(colorId)
    if color:
        if current_user.is_admin or current_user.is_staff:
            db.session.delete(color)
            db.session.commit()

    return jsonify({})

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
@cars.route("/adm/users/", methods=["GET", "POST"])
def register_owner():

    if request.method == "GET":
        models = Model.query.all()
        colors = Color.query.all()
        models = Model.query.all()
        users = User.query.all()

        owners = []
        for u in users:
            obj = {
                'id': u.id,
                'first_name': u.first_name,
                'last_name': u.last_name,
                'email': u.email,
                'qtd_cars': len(u.cars)
            }
            owners.append(obj)

        return render_template(
            'owners.html', 
            user=current_user,
            owners=owners,
            models=models,
            colors=colors
        )

    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name  = request.form.get("last_name")
        email      = request.form.get("email")

        if len(first_name) < 1:
            flash("First name is too short!", category="error")
        elif len(last_name) < 1:
            flash("First name is too short!", category="error")
        elif len(email) < 7:
            flash("Email is too short!", category="error")
        elif email.find('@') == 0:
            flash("Email is not correctly", category="error")
        # elif color == None:
        #     flash("Color need to be choosen", category="error")
        # elif model == None:
        #     flash("Model need to be choosen", category="error")
        else:
            # creating user
            new_user = User(
                first_name=first_name, 
                last_name=last_name,
                email=email,
            )
            db.session.add(new_user)
            db.session.commit()

            flash("User registered!", category="success")

    return redirect(url_for('cars.register_owner'))

@login_required
@cars.route("/register-car/<id>/", methods=["GET", "POST"])
def register_car(id):
    user = User.query.filter_by(id=id).first()

    if not user:
        flash("User not found", category='error')

    if request.method == "POST":
        color      = request.form.get("color")
        model      = request.form.get("model")

        if color == None:
            flash("Color need to be choosen", category="error")
        elif model == None:
            flash("Model need to be choosen", category="error")
        elif len(user.cars) > 2:
            flash("An user can be the maximum of 3 cars registered", category='error')
        else:
            # creating car
            new_car = Car(color_id=color, model_id=model, owner_id=user.id)
            db.session.add(new_car)
            db.session.commit()
            flash("Car registered!", category="success")

    return redirect(url_for('cars.register_owner'))

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
