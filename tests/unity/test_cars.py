from venv import create
import pytest
from website.models import Car, Model, Color
# from . import db
from flask import url_for

from app import create_app

def app():
    app = create_app()
    return app

class TestCar():

    def test_pytest(self):
        '''
        test module pytest
        '''
        assert 1 == 1

    def test_create_car_without_owners_gets_wrong(self):
        '''
        try to creates a car without owner
        '''
        pass


    def test_create_car_owner_email_already_exist(self):
        pass


    def test_create_car_without_owner_return_error(self):
        pass