# EPICEVENTS

Openclassrooms - Parcours développement Python Projet 11

## Status

This project is under development.

## Description

EpicEvents is an API is organized around  [REST](https://fr.wikipedia.org/wiki/Representational_state_transfer). This API has predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

The **documentation of the API** is available at the following [location](https://documenter.getpostman.com/view/14947762/TzJu9x5r).

This project uses the following technologies:

* [Python](https://www.python.org) as the programming language
* [Django](https://www.djangoproject.com/) as a web framework
* [Django REST Framework](https://www.django-rest-framework.org/) as a REST API framework
* [Pytest](https://pytest.org) and [Coverage](https://pypi.org/project/coverage/) for testing
* [Postgresql](https://www.postgresql.org/) as a database

## Database

The API allows interfacing with a database that contains the following tables:

* `User`: contains information about the API Users
* `Group`: contains inforamtions about the groups of users used to definme permissions for accessing the data from the different tables.
* `Client`: Contains the data related to the clients of Epic Events.
* `Contracts`: Contains the data related to the contracts signed by the clients of Epic Events.
* `Events`: Contains the data related to the events organised by Epic Events after a contract is signed.

The Entity Relations Diagram is the following:
![ERD](ERD.png)

## Installation

Python 3 and postgresql are required to run the API.

1. Clone this repository (or download the code [as a zip file](https://github.com/antoine71/epicevents/archive/main.zip)):

```shell
git clone https://github.com/antoine71/epicevents.git
```

2. Navigate to the root folder of the repository.
3. Create and activate a virtual environment:

```shell
python -m venv env
source env/bin/activate
```

4. Install project dependencies:

```shell
pip install -r requirements.txt
```

5. Create a postgresql database.

```shell
createdb epicevents_db
```

6. Modify as required to suit the requirements of your system the settings to connect to the database from the file `config/settings.py`

```python
...
DATABASES = {
    'default': {
        ...
        'NAME': 'epicevents_db',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
...
```

7. Start the postgresql server

```shell
sudo service postgresql start
```

8. Apply the migrations to the database

```shell
python manage.py migrate
```

9. Create a superuser

```shell
python manage.py createsuperuser
```

10. Run the server

```shell
$ python manage.py runserver
```

## Usage

The api can be queried from the following address: http://localhost:8000/api/

All the API endpoint details are provided in the [API documentation](https://documenter.getpostman.com/view/14947762/TzJu9x5r).

## Testing

* The repo is provided with a full test suite in the folders `epicevents/events/tests/` and `epicevents/users/tests/`. This test suite provide 100% coverage. The tests can be run using the following command from the root folder of the project:

```shell
pytest
```

* A full test report can be generated in html format thanks to the utility Coverage. Coverage will create a new folder named `htmlcov`. Open the file `htmlcov/index.html`to view the report. To generate the report, from the root folder of the project, run the following commands:

```shell
coverage run -m pytest
coverage html
```
