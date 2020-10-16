# ETL Covid

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
python -m etl_covid 5
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
docker-compose run --service-ports --rm test
```

#### Run
```sh
docker-compose run --service-ports --rm dev
```
