# ETL Covid

## Setup
```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Workflows

### Local Development

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


### Continuos Integration
