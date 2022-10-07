#!/bin/bash

# Remove all database-related files 
cd Growing_Enterprises
find . -type f -regex ".*__pycache__.*" -exec rm {} \;
find . -type f \( -regex ".*migrations.*" ! -name "__init__.py" \) -exec rm {} \;
find . -type d -regex ".*migrations" -execdir touch "{}/__init__.py" \;


# Run migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Fill database
python3 manage.py initdb
