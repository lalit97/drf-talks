# DRF Talks

django and django-rest-framework discussions.

## Local Setup

- Git clone: `https://github.com/lalit97/drf-talks.git`
- Go to the project directory: `cd drf-talks`
- Setup virtual environment: `python3 -m venv env .` (do not forget to add the dot(.) in the end)
- Activate virtual environment: `source env/bin/activate`
- Install requirements: `pip install -r requirements.txt`
- Run migrations: `python manage.py makemigrations`, `python manage.py migrate`
- Run server using local settings: `python manage.py runserver`
- See it running on [localhost](http://127.0.0.1:8000/)
