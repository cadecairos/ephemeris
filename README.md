# Ephemeris

A prototype Django application for managing event schedules

FYI: Ephemeris is the latin word for calendar.

## Getting started

### Prerequisites

* git
* Python 3
* virtualenv
* Node 4.4.7+

### Dev Environment

First Clone the repository: `git clone git@github.com:cadecairos/ephemeris`

Get into the project directory: `cd ephemeris`

Set up your virtual environment: `virtualenv env`

load the virtual environment: `source env/bin/activate`

Install python dependencies: `pip install -r requirements.txt`

Install front-end dependencies: `cd app/ephemeris_app && npm install`

Build + watch the front-end: `cd app/ephemeris_app && npm start`

(new terminal) Run the dev python server: `cd app && python manage.py runserver`