# How to use project?

* clone this repository

```commandline
git clone https://github.com/SabirzhanovN/OnlineShopLesson.git
```

```commandline
cd OnlineShopLesson
```

* create virtualenv
```commandline
python -m venv venv
```

* Then activate them
```commandline
source venv/bin/activate
```

* Install all dependences
```commandline
pip install -r requirements.txt
```

* Migrate model to DB
```commandline
python manage.py makemigrations
python manage.py migrate
```

* Create your super user
```commandline
python manage.py createsuperuser
```

* And now start this project!
```commandline
python manage.py runserver
```

## Congratulations! You're finished!