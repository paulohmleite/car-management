from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# from website.models import Car, User, ColorCar, ModelCar

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    # app = Flask(__name__, static_folder='../static')
    app = Flask(__name__,)
    app.config["SECRET_KEY"] = "HFSDIOGHIODMODFGHJDIOFJOI"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .cars import cars

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(cars, url_prefix="/")

    from .models import Color, Model, Car, User

    with app.app_context():
        if not path.exists("website/" + DB_NAME):
            db.create_all()
            print("Created Database!")

    # how reload a user
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")
