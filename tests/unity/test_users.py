from website.models import User
import pytest
from pytest import mark


@mark.parametrize(
    "password,valid",
    [
        ("abcde12345", True),
        ("12345678", True),
        ("abcdefgh", True),
        ("abc12345", True),
        ("12345abc", True),
        ("11111111", True),
        ("22222222", True),
    ]
)

def test_validate_password_general(password, valid):
    '''
    testing the model user
    '''
    # given
    user = User(email='email@email.com', first_name='email', password=password)

    try:
        user = User(email='email@email.com', first_name='email', password=password)
        assert valid

        assert user is not None
        assert user.email == 'email@email.com'
        assert user.password == password

    except:
        assert not valid

def test_missing_fields():
    # given
    data = {
        "email": "maria@email.com",
        "password": "Abcde12345"
    }
    # when / then
    try:
        user = User(data)
        assert False
    except:
        pass