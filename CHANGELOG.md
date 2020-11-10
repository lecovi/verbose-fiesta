# Change Log

## v0.0.1

- Simple Flask Hello World application. Running with `poetry` or `pipenv`.

## v0.0.2

- Adds Dockerfile using Python 3.7

## v0.0.3

- Updates Dockerfile with Python 3.8
- Adds CHANGELOG

## v0.0.4

- Adds docker-compose.yml

## v0.0.5

- Adds Database support
    - `GET /create_db` endpoint for creating DB schema
    - `GET /users/` endpoint for getting all users
    - `GET /users/{{pk}}` endpoint for getting users with id=pk
    - `POST /users/` endpoint for creating users with username and email
- Changes Docker image from Alpine to Debian Slim Buster