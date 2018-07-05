# About
Program sederhana untuk mengolah data Praktik Kerja Lapangan (TKJ, RPL) :D.
Pengembangan dari [esp](https://github.com/hilmizul/esp).

# Requirement
* Python 2.7.x
* Django 1.10.x, 1.11.x

# Setup
* Download [epkl-master.zip](https://github.com/HilmiZul/epkl/archive/master.zip)
* Extract. Open Terminal.
* ```cd epkl/```
* ```./manage.py makemigrations && ./manage.py migrate```
* ```./manage.py createsuperuser```
* ```./manage.py runserver```
* Go to ```http://127.0.0.1:8000```

# How to use
## Add an account
* Go to [http://127.0.0.1:8000/dapur](http://127.0.0.1:8000/dapur).
* Enter username and password you created before.
* Go to ```Akun``` and then ```Add```.
* Input username from django User.
* Save & Done.

## Login to main system
* Go to [http://127.0.0.1:8000](http://127.0.0.1:8000).
* Enter username and password you created before.
