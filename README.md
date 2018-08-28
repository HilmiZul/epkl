# About
Program sederhana untuk mengolah data Praktik Kerja Lapangan (TKJ, RPL) :D.
Pengembangan dari [esp](https://github.com/hilmizul/esp).

# Requirement
* Python 2.7.x
* Django 1.10.x or 1.11.x
* Lib.xlwt
* libmysqlclient-dev, mysqlclient

# Setup
* Create new database e.g. ```pkl```
* Download [epkl-master.zip](https://github.com/HilmiZul/epkl/archive/master.zip)
* Extract to ```~/```. Open Terminal.
* Debian/Ubuntu: ```sudo apt-get install libmysqlclient-dev```
* ```pip install mysqlclient```
* ```pip install xlwt```
* ```cd epkl-master/```
* ```chmod +x manage.py```
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

# Thanks to
* Haturnuhun Kang Vitor Freitas yang udah bantu untuk export XLS :D [reference](https://simpleisbetterthancomplex.com/tutorial/2016/07/29/how-to-export-to-excel.html)
