# superheroes-code-challenge
This project is a Flask REST API that manages superheroes, their powers, and the relationships between them. It fulfills all requirements outlined in the Superheroes Code Challenge rubric, including proper model relationships, validations, and RESTful routes.

# Tech Stack

Python 3

Flask

Flask-SQLAlchemy

Flask-Migrate

SQLite

SQLAlchemy Serializer

Setup Instructions
# Clone repository
git clone <repository-url>
cd superheroes-code-challenge

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Database setup
export FLASK_APP=run.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Seed database
python3 -m app.seed

# Run server
python3 run.py


Server runs at:

http://127.0.0.1:5555


# API Endpoints 
# Heroes 

GET /heroes
Returns a list of all heroes.

GET /heroes/<id>
Returns a single hero with associated powers.
Returns 404 if hero is not found.

#  Powers

GET /powers
Returns a list of all powers.

GET /powers/<id>
Returns a single power.

PATCH /powers/<id>
Updates a power’s description.
Validation: description must be at least 20 characters.

# Hero Powers 

POST /hero_powers
Assigns a power to a hero with a specified strength.

Valid strengths

Strong

Weak

Average

Returns the updated hero on success.

# Validations & Error Handling 

Invalid data returns appropriate error messages and HTTP status codes.

Missing resources return 404 Not Found.

Strength values are strictly validated.

# Testing 

All endpoints were tested using Postman.
A Postman collection is included in the repository.

# Author

Festus Kisoi
Full-stack Developer
Flask • SQLAlchemy • REST APIs