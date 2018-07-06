# django-template

### How to quick start new project:
    1. git clone git@github.com:mmasterenko/django-template.git
    2. virtualenv -p /usr/bin/python3 venv3
    3. add the snippet to the end of venv3/bin/activate
    4. mv .env.example .env
    5. source venv3/bin/activate
    6. pip install -r requirements.txt
    7. ./manage.py migrate
    8. ./manage.py runserver


### DATABASE_URL example

    DATABASE_URL='postgres://user:password@localhost/dbname'


### snippet for activate

    ENV_FILE='/path/to/.env'
    export $(cat $ENV_FILE | xargs)


