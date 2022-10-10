# Documentação

# car management
## Dados

The fist user created on sign up will be the admin user. That user can do anything.

* Users from staff or admin can register new owners.

> only users staff can change data 
## I have tried to implement using socker compose but I hadn't time for fix the errors, so it doesn't work for now.
## without docker windows

you can run the project without docker by the next steps on terminal powershell:

* `python -m venv venv`: for creating environmental ambient
* `. /venv/Scripts/activate`: for active the environmental
* `pip install -r requirements.txt` : for installing the packages
* `flask run` : for running the flask project

## tests

For testing I use pytest

* `pytest --cov .`: run the tests

## guide 

Here we have the login page
![](2022-10-09-20-09-12.png)

Type SIGN UP and create your account, the **first account created will be the admin**.
![](2022-10-09-20-09-45.png)

Here we have the home page with logged in user
![](2022-10-09-20-11-06.png)

In the menu in administration -> car colors, create your colors. [Yellow, Blue, Gray]
![](2022-10-09-20-12-55.png)
![](2022-10-09-20-29-38.png)

In the menu in administration -> car models, create your models. [Hatch, Sedan, Convertible]
![](2022-10-09-20-29-57.png)

Now you can go to menu administration -> car owners to register the owners, you will notice there is a user, you.
* for add cars to an existing user, hit ADD button.
* For add a new owner register bellow the table.
* in the table if your has an exclamation, it means that user can be a possibly sale.
![](2022-10-09-20-38-39.png)

