# verbose-fiesta
A Flask Hello World example with a database!

## Install

```bash
poetry install
```

You can use `pipenv` if you prefer.

## Docker Compose

Create `.env` from `env.dist`.

Build:

```bash
docker-compose build
```

Run:

```bash
docker-compose up
```

Your app running port is defined with `FLASK_RUN_PORT`. You can check PGAdmin over `PGADMIN_PORT` at localhost.

# Versions

See [CHANGELOG](CHANGELOG.md) for more details.
