# Starter Python Project

This is a starter Python repo, for a dockerized cloud Python application, using Git Actions for Continuos Integration.
It uses docker-compose with a PostgreSQL service container.

## Setup
```sh
# Start a clean python environment
pipenv shell

# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Workflows

### Local

Running directly in the development computer.

#### Test
```sh
# Executes all the tests
py.test
```

#### Run
```sh
# Executes the module with argument 5
python -m py_start 5
```

### Container

Running using containers in the development computer.

<!--
#### Run only the database server
```sh
docker-compose run --service-ports --rm db
```
-->
#### Buid Image
```sh
# Builds the application docker images
docker-compose build
```

#### Test
```sh
docker-compose run --service-ports --rm test 5
```

#### Run
```sh
docker-compose run --service-ports --rm dev 5
```
