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

The Entity Relations Diagram is the following, also available at the following [location](https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=ERD.drawio#R7Z1bc6M4Fsc%2Fjat2H5LiYoj9mDhOT%2B9216Y6vbuz85JSG8WmBxALcmL3px8JBL4IOxAMEoKqzLQRWGD9j366nSNG5szffIpAuPqKHOiNDM3ZjMz7kWHoN7ZB%2FqEp2zRlPB2nCcvIddhFu4Qn9xdkiRpLXbsOjA8uxAh52A0PExcoCOACH6SBKEJvh5e9IO%2FwriFYQi7haQE8PvW%2FroNXaerE0nbpv0F3ucrurGvsjA%2Byi1lCvAIOejtIghv8gALMHvERRj4IYIDJma8g%2BhNGI2u%2Bwpj%2B0tuR8UD%2BXujV10uElh4EoRtfL5BPkhcxueThBfiuR4t5L6M7lhG5nTkfmbMIIZx%2B8jcz6FGtMhnSZ3o4cTYvh4jmW%2BIL5v1cD9%2Fm8%2FvPwe9w%2FYfzpP%2F4zxXL5RV4a1a%2B%2F47TpyPlg7dZoZOiCulHDH7QpLsYgwgz2zA1kkDUxsANyFfNez059jwQxm5yeZqycj3nC9iiNc4yyo7uXtwNdL6lpkGvJVbyhWRGD2nmtJCf2MPQ08BzlwH5vCC%2FnN7xLoIxeZYvIMbsCr5ssh8KIww3e0msrD5B5EMcbckl7OyVmVk8qyj58dvO7AyTpa32TM6YsETA7GiZZ76Th3xgClVQy%2BDUOqkU%2Be3YBd43UgVBsExEO9SEFqwTofA7iJYQs4QQubRI568wrQRJ6bueN0MeotIGKKA5YRSykx58yb77A2FMjJ8pyIojzzQpCuuO%2FJHCmWnX1sgijzsjx%2FrumPzRyyM8Q0GMI2JQNA9IdH2DVNsCXc9a9ftiZ9qWlNZsSlmTU%2Fbxn9W0TWgLdtpWlk07ku241iFSnC9eAsyV6zgwKK%2BHUVqPPQFaLf8xV%2F5rwsFn8h2xImSoS6%2B9i0OwcIPll%2FSb9pFKVlsqbU7XGq1N1axO8PBY0w7w0BbNQ7umsheviNBxs%2FxqwtAqLYYoGN4UwjAAPkz6vdpsBaIHF3rO33RL%2B7vshGxFKlmIOBmI2AwRp6KJOFWXiJPSYogiYjb02yv9EMTxG4ocDonGRGUkltdKFiTq%2FBzHwMSLMFE3RENRrzsjIjEV9fJ6CMMiP20BfeB6o5kxuiU31eb0KOGiwkisIJQsTDT4Lv7AxMsw0RLNRKPuGEBiJuZ2Ky8TDb6j%2FuJGMX7u4fi5glyykNHke%2FoDGS9DxoloMpp1RwISkzG3W3nJaPKddQ%2FsgTHpNPaGjRUEE8DGf%2Fz6ZdgYPlyZ1v8%2F3%2F%2Fc4NfHRYGzwIDGi6DRKOta0Ji0aoyjz1qtFGAsfEJ%2BFO3GzzEGLy9pf%2FEOIQ%2BCQKFxdE2hZAEi7zUwAPEyQByLBiLvWvAg2iGnBBIPfXbKVbtxaXFE8ZF3BlhGaB12EYXNCiTNIJpv0Waem%2Fi%2FnpCsR46lR26l46IJQ6tIrZvG5OpGOyberzS361qOpYXiNqYt35Cp5FlqStV6FT8i33wtEhj2y7u0glJnmjGjVeWGVbKmuFjkYNouFxVeJTPlXyUzq6ySGZbSE8EXWSRrFYzZ6HwA48XBWORn2ioYxwovkuV2Ky8Yx%2FxM%2FMEiWX%2B4WEEsWbg4qeukPXDxFBcLfU1bBeO0bqMnMRhzw5UXjFO%2BXUp9TRMo9sLRtIJKshBxyjdnAxEvRMTSE8eNictP8ytDxNxwJSYiP20frpJSo0TkOotKe1NVkEsaNA7R642hscjVtF00KhzAPpU%2Fgn3Kz9z76Ifr9ZONFwljb5eNQxx7U2ws9DVtl40Kh7JPuxDLzk9kkDJNnthR1eG0rliygFHXBif8xshY5HTaKhl1re50icRo3JmuzGzkpzQWyA9BsN1bgeGiODWl%2B49VhJOHk93waewkJ2%2FEc7Lu3InUnJTfp1HX%2BPkNB2D4vIggyLuR9%2BTjd9eHqvcjqygmDyAH58amAGlq4gGpsHvjznRlBiQ%2FyZEAch06fQRkB30c6y5uDnw8yUfhUTFjfnSgQHjneTuWF5ZjvjcfAw%2FGz0nw36ILgTIC1JIGlPxQgBCFAGUxhHvuw67qLGNzrxEZd6PrLz7eMzft7sR7jvmOv0rxnmP5u%2F5jvue%2FYDzsQEN2wYjPClrJ0pZZQ6e%2FKTIKj%2Fi06q4ISDwlYsnfybf4Tn4YoZ%2BkSIt3RlV7Ta2CYALYWLxL2RDc1BQb2wz6LN5iSI3YpvN2KwUbi4ufd%2BqJCXvUdceqK5Qs%2FUW9YHudAYqXgaL4iE%2B9YOueLmLxHdOVgosnnpGfqQI%2BWtMfRsH44CGAFcJibaFk4aI19BUbw6LwsE9bjc7iecOVF4o231kMwdanG8o5a%2FhM3Qv65V1QQTNZ%2BKgXvFBwAOSFACk8%2BFOv%2FcpBiQm5M115EakXvBewx%2B6pFRSTB5DDSkxTgBQfAarrCq%2FF7ExXZkDy81Y9dk%2BtoJgsgLTqTk0NfDzJR%2BFxoBY%2F7aWqe6pVXh5hK9e8S1VnNnAXIJMshLT5MUDCspOS9cgp9egdJHrZgKXmfFLtbvT3xfuk5mbdHZ9Um%2B%2Ftq%2BSTasvf37f57n4%2FfVIraCVNOzb09Jsio3CfVLtuJIbE8yC2%2FD17m%2B%2FZA4xh4EDaPaNTIJ9JxVjCSPUZkApaSYPFwcWgKSwKfwdJtsGMkliU38PgpmCr%2FdfEv6B3vgUV1JIFjLo%2BkLEpMkrgk2oozMad6coLR93g6RggnHUYv8ON%2Bh6pFWSShoomPx08UPFCVBTukqoXvHFcHSqa5RUR56nPz%2FHSjVM92LdNpauoJQ0cjQGOjcFRvDuqoTIcjQ7A0eDh2GN31AqKyQPIIc6zKUBK4I5qqBznaXQgztPg18F67I5aQTFZADkZFqkb46Nwd9RJf9xRJ%2FIvWk%2F4Ret1DKMO%2BPEIEEkWPupGiQ3ZobOEWVmQEnDx9hv0AHZRMN%2BdSUss9U7VyU%2B%2BW2HfY7UABs5tFCUFPP%2F2C0boO%2FoKgu2I%2BbTuzvkgcP6VSEzuE21%2FzyoVPfgfPbi2ssP7zf7J%2By07%2Brn2Q%2FYUdnpndjQZHXrQ5scPLi2yNKuNi%2Bk99WtNM9hxetsJO9rdlR5s9w4eYUT6AIlrLHssh%2BV81jc2RutoAc8oxOTAWZtz6rpsh14qVlk%2B5P61%2B7aWJ0aJyK%2Fw4HmLLJDd45E2WjvbvrpheM7cPTN3yyyL9Kezb%2B3smM8oa2hYRuNjZ9%2B0bLiMkgqR%2F%2FA6daTEwmVbdYQRMLfUAyu1zlupiCr1ccPPZm7ftfwsBkAayz92Yze0I4Mta%2Fn5CztYRtZxRk1bftbutGf5uxbg%2FaZBr2bHWZ3RKtSZj5tvtsvsu%2BZrywbu8c2R%2BRofNF%2FjKCNz2rb5ltjvYAB3RXBLY6dXkyPzyhqCqnaqv5PP5cy0cH%2FBgj1XPkVoHXKm2sOAsCvbOGoCizydisa5%2BnFbebFdMWvvoqJgSNh5w64VEtbqjqcFG7R0NCTsvOlKMY1U%2FIj8ovCS0rAD80gfiwerK9SZqaSi1rc54YY32zaFxaJ4sHYrpRrvtT1vtxIzkV%2FFKnw3gaXKuwnqCiULE02pZtcPzp0fDX5smLo%2F470%2Fniw9A362LZRn4GkezUhbWRx75altU38np4bHnmO%2BvzsP3QVrYg3t9vEz%2Bf8V%2BW%2BemCb5kFknPX3vgmUEfM6mSf3Eh0ZKGkz0JzxiSwFuuFElre3uAni37IRPqJHUiLeVi%2BETAQy951sEwmTIug4c6pex6zinNm1YXEf6AoPTPCLx9PDFLmoojifUSvCGHEYI4X31yU9efUUOpFf8BQ%3D%3D):

![ERD](ERD.png)

## Installation

**Python 3** and **postgresql** are required to run the API.

1. Clone this repository (or download the code [as a zip file](https://github.com/antoine71/epicevents/archive/main.zip)), navigate to the root folder of the repository, create and activate a virtual environment, install project dependencies:

```shell
git clone https://github.com/antoine71/epicevents.git
cd epicevents
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

2. Create a postgresql database and start the postgresql server.

```shell
createdb epicevents_db
sudo service postgresql start
```

3. Modify as required to suit the requirements of your system the settings to connect to the database from the file `config/settings.py`

```python
...
DATABASES = {
    'default': {
        ...
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
...
```

4. Apply the migrations to the database and create a superuser

```shell
python manage.py migrate
python manage.py createsuperuser
```

5. Run the server

```shell
$ python manage.py runserver
```

## Usage

The api can be queried from the following address: 
```
http://localhost:8000/api/
```
The following endpoints are available:
```
api/auth-token/ # POST
api/clients/	# GET, POST
api/clients/me	# GET
api/clients/prospects	# GET
api/clients/{pk}/	# GET, PUT, DELETE
api/clients/{pk}/contracts/	# GET, POST
api/contracts/	# GET
api/contracts/me	# GET
api/contracts/{pk}/	# GET, PUT, DELETE		
api/contracts/{pk}/events/	# GET, POST
api/events/	# GET	
api/events/me	# GET					
api/events/{pk}/	# GET, PUT, DELETE
```

All the API endpoint details are provided in the [API documentation](https://documenter.getpostman.com/view/14947762/TzJu9x5r).

## Administration

The API is provided with an web administration interface. This interface is accessible to all users with the `staff` permission.
```
http://localhost:8000/api/admin/
```

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
