from venv import create
import pytest
from website.models import Car, Model, Color
# from . import db
from flask import url_for

from app import create_app

def app():
    app = create_app()
    return app


# def create_basic_colors():
    # yellow = Color(color='Yellow')
    # db.session.add(yellow)

    # blue = Color(color='Blue')
    # db.session.add(blue)

    # gray = Color(color='Gray')
    # db.session.add(gray)

    # db.session.commit()

    # return yellow, blue, gray

# def app():
#     app = create_app()
#     return app

# def test_myview(app):
#     client = app.test_client()

#     assert client.get(url_for('/login')).status_code == 200



class TestCar():

    def test_pytest(self):
        '''
        test module pytest
        '''
        assert 1 == 1

    # def test_create_color_yellow_return_success(color):
    #     '''
    #     test for success creating a new color
    #     '''
    #     # yellow = Color(color='Yellow')
    #     # db.session.add(yellow)
    #     # db.session.commit()

    #     # y = Color.query.get(color='Yellow')

    #     assert color == 'Yellow'
    def test_create_car_without_owners_gets_wrong(self):
        '''
        try to creates a car without owner
        '''
        

        car = Car()