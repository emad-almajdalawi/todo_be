import os
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from flask_cors import CORS
from routes.todo_routes import todo_routes


def create_app():
    """
    Creates the flask app

    Return:
        - app: the flask application's object
    """
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KYE")
    CORS(app)
    return app


def db_connet(app):
    """
    Connects to MogoDB

    Args:
        - app: the falsk application's object

    Return:
        - mongo: the thedabase's object
    """
    app.config["MONGO_URI"] = os.getenv('MONGO_HOST')
    mongo = PyMongo(app)
    return mongo


def load_routes(app):
    """
    Calls all routes functions

    Args:
        - app: the flask application's object
    """
    todo_routes(app)


def run_flask(app):
    """
    Runs the flask application

    Args:
        - app: the flask application's object
    """
    load_dotenv()
    app = create_app()
    mongo = db_connet(app)
    app.mongo = mongo

    load_routes(app)
    app.run(debug = True)


if __name__ == "__main__":
    run_flask(create_app())
    