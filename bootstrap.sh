#!/bin/bash
export FLASK_APP=./backend/wsgi.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0
