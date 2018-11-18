# Django tutorial app

> Simple Polls app in Django

Manage environment using virtualenv wrapper

```
mkvirtualenv env -p `which python3`
workon env
```

Install postgres db
```
brew install redis postgresql
```

Install requirements

```
pip install -r requirements.txt
```

Migrate and Run server

```
python manage.py migrate
python manage.py runserver
```
