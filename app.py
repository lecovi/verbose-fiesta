import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request, url_for
from flask_sqlalchemy import SQLAlchemy


load_dotenv()


__version__ = os.environ['VERSION']


def get_db_uri():
    """Returns DB_URI from environment variables
    """
    DB_SERVICE = os.environ['DB_SERVICE']
    DB_USER = os.environ['DB_USER']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ['DB_PORT']
    DB_NAME = os.environ['DB_NAME']
    DB_URI = f'{DB_SERVICE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    return DB_URI


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = get_db_uri()
db = SQLAlchemy(app=app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<{self.__class__.__qualname__} {self.username}>"

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

    @classmethod
    def get_by(cls, **kwargs):
        return db.session.query(cls).filter_by(**kwargs).first()

    def save(self):
        db.session.add(self)
        db.session.commit()


@app.route('/')
def hello_world():
    return f'Hello World!! v{__version__}'


@app.route("/create_db")
def create_db():
    if not db.engine.dialect.has_table(db.engine, User.__tablename__):
        db.create_all()
        app.logger.info("Database Schema Created...")
    
    pg_version = db.engine.execute('SELECT version();').scalar()
    return jsonify({"db_version": pg_version})


@app.route("/users/", defaults={"id": None})
@app.route("/users/<int:id>")
def get_users(id):
    response = []
    if id is None:
        users = User.all()
        for user in users:
            response.append({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "url": url_for("get_users", id=user.id)
            })
        return jsonify({"users": response, "total": len(response)})

    user = User.get_by(id=id)
    response = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "url": url_for("get_users", id=user.id)
    }
    return jsonify({"user": response, "total": len(response)})


@app.route("/users/", methods=("POST",))
def create_user():
    payload = request.get_json()

    try:
        username = payload["username"]
        email = payload["email"]
    except KeyError:
        return jsonify({"error": "Missing 'username' or 'email'"}), 400

    user = User.get_by(username=username)
    if user is not None:
        return jsonify({"error": "This 'username' already exists"}), 409
    user = User.get_by(email=email)
    if user is not None:
        return jsonify({"error": "This 'email' already exists"}), 409
    
    user = User(username=username, email=email)
    user.save()
    app.logger.info(f"<{user.__class__.__qualname__} id={user.id}, username={user.username}>")
    response = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "url": url_for("get_users", id=user.id)
    }
    return jsonify(response)

