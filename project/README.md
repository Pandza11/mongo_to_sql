# An ETL script for AWW

This is an ETL script for A Web Whiteboard by GoodCode.

### Quickstart

Get the source from GitHub:

    git clone https://github.com/dobarkod/aww-etl.git

Create Python3 virtual environment:

    mkvirtualenv --python=/usr/bin/python3 etl

Install required files:

    pip install -r requirements.txt

Create '/etl/.env' file to define environment variables
showed in .env.sample, for example:

    DEBUG=true

Migrate the database:

    python manage.py migrate

Create superuser:

    python manage.py createsuperuser

Run development server:

    python manage.py runserver

Point your browser to http://127.0.0.1:8000/admin and login
