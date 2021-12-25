About
====

Webapp demo for cloud computing predavanja.

Milena Laketić

R2 22/ 2021

Installation
====

This project doesn't require system wide installation, simply clone its repository to get started::

``` 
  $ git clone https://github.com/specnazm/cloud-computing
  $ cd cloud-computing
  $ poetry install
```


Quick-start
====

Setup the database (PostgreSQL)

Create .env file in root folder and define
```
  DB_PASS=yourpassword
  DB_USER=yourusername
  SECRET_KEY=djangosecretkey
```

Afterwards run command
```
  export $(xargs < .env)
```

Setup the database, run Django migrations and create Django superuser::
```
  $ poetry run python manage.py migrate
  $ poetry run python manage.py createsuperuser
```

Run the webapp server, in development mode:
```
    $ poetry run python manage.py runserver
    $ xdg-open http://localhost:8000/
    $ xdg-open http://localhost:8000/admin
```
