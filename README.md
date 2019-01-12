# Bungalow Challenge API

## Development Setup (The usual Django stuff)

### Prerequisites

1. MySQL Server installed and running locally with default config.
    - Can also change the database config in `bungalow/settings.py` to point to a different MySQL URI (cloud host, etc)

### Setup Instructions

1. Create a virtualenv
2. pip install -r requirements.txt
3. Create a new database 'bungalow' in the connected MySQL Instance (or a
   different name, but change the DATABASE settings)
4. python manage.py migrate
5. python manage.py ingestcsv challenge_data.csv # Populate your database with
   the seed data
6. python manage.py runserver

Navigate to `http://localhost:8000/api/rentals` to use the API.
