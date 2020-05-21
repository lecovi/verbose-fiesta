# verbose-fiesta
A Flask Hello World example

## Install

```bash
poetry install
```

You can use `pipenv` if you prefer.

## Run

```bash
poetry run flask run --host=0.0.0.0
```

### Docker

Build:

```bash
docker build . -t verbose-fiesta:0.0.2
```

Run:
```bash
docker run --rm --name verbose-fiesta -v $PWD:/usr/src/app -p 5000:5000 verbose-fiesta:0.0.2
```
