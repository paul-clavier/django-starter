# django-starter

This repository aims to be cloned for anyone willing to start a new django project easily
To get started use the following

## Installation

Install [pipenv](https://pipenv.pypa.io/en/latest/)

```
pipenv install --dev
```

## Setup

Check for migrations
```
pipenv run python3 manage.py makemigrations
```

Run migrations
```
pipenv run python3 manage.py migrate
```

Start the environment
```
pipenv shell
```

Create a first super user
```
pipenv run python3 manage.py createsuperuser
```

## Start
```
pipenv run python3 manage.py runserver
```

## Tests
```
pipenv run python3 manage.py test
```