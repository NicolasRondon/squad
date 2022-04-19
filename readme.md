# Squad Makers

Jokes API is an api to get random jokes

## Python Version
`3.9.6`

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install crehana-partners.

```bash
pip install -r requirements/base.txt
```

## How to set up dev tools
* install dev requirements  `pip install -r requirements/dev.txt`
* run  `pre-commit install`




## How to run server?
`python manage.py runserver`


## How to test?
First, install requirements from requirements/test.txt

Create empty databases in order to store data generated the tests. It is okey if is empty, because at the end of the tests, all the tables are detroyed. After that, run:

`pytest tests`

## How to view coverage?
First, install requirements from requirements/test.txt

Instead of running tests with the command below, use:
`pytest --cov=jokes_api tests/`.
After that, you can run
`coverage html` in order to generate html directory located in htmlcov (which includes an index.html file)

## Environment variables
Additional settings could be found in the following file `jokes_api/config/settings.py`

| Var | Description | required |
| ------ | ----------- | -----
| PARTNERS_DB_URL   | Users API BD | true
| CREH_SETTINGS_MODULE | Settings file which contain config | true
| DATABASE_URL   | Monolithic Crehana DB. |true
| SENTRY_DNS   | For alerts  | false
| LOG_LEVEL   | DEBUG, INFO, WARNING or ERROR  | false
