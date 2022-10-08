import pytest
from website.models import db
from sqlalchemy import delete
from website.models import Color, Model, Car, User

from app import create_app
from werkzeug.security import generate_password_hash, check_password_hash


@pytest.fixture(scope="session")
def flask_app():
    # setup
    app = create_app()

    client = app.test_client()


    ctx = app.test_request_context()
    ctx.push()

    yield client

    # tear down
    ctx.pop()

@pytest.fixture(scope="session")
def app_with_db(flask_app):
    db.create_all()

    yield flask_app

    db.session.commit()
    db.drop_all()


@pytest.fixture
def app_with_data(app_with_db):
    color_car = Color()
    color_car.color = 'Yellow'
    db.session.add(color_car)

    model_car = Model()
    model_car.model = 'Hatch'
    db.session.add(model_car)

    user = User()
    user.first_name = 'Paulo'
    user.password = generate_password_hash('pass')
    user.email = 'paulo@email.com'
    db.session.add(user)

    car = Car()
    car.model_id = model_car
    car.color_id = color_car
    car.owner_id = user
    db.session.add(car)

    db.session.commit()

    yield app_with_db

    db.session.execute(delete(User))
    db.session.execute(delete(Car))
    db.session.execute(delete(Model))
    db.session.execute(delete(Color))
    db.session.commit()




