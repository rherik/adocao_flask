#!/bin/sh

flask db upgrade

gunicorn 'app:create_app()' --bind 0.0.0.0:5000 --reload