# ChoppedUp for game jam

This is backend part for ChoppedUp Game (ios)
using django for game content management.



Features:

On admin page, administrator has access to add/edit/disable/enable content for client side.



Requirements:

Django 1.10.4, and Python 3.5



Quick Start: Test on your local:

$ git clone git@github.com:zoe-stockholm/ChoppedUp.git
$ pip install --upgrade virtualenv
$ virtualenv ChoppedUp
$ source ChoppedUp/bin/activate

go to your project root (ChoppedUp)

$ pip install -r requirements.txt
$ python manage.py migrate

To log in, you need to create a superuser - a user account that has control over everything on the site.
Go back to the command line
$ python manage.py createsuperuser
follow the steps to finish super user creation

when it's done, in the project root
$ python manage.py runserver

You can login admin panel http:127.0.0.1:8000/admin with the username and password you created minutes ago.
see the example below:
username: admin, password: feomedia
