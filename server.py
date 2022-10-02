from flask import Flask
import os
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from routes.todo_routes import load_routes


def create_app():
    """
    Creates the flask app
    Return:
        - app: the flask application's object
    """
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KYE")
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


def run_app(app):
    """
    Runs the flask application
    Args:
        - app: the flask application's object
    """
    app.run(debug = True)


def initiate_routes(app):
    """
    Calls all routes functions
    Args:
        - app: the flask application's object
    """
    load_routes(app)


def initiate_flask(app):
    """
    Calls all needed functions to run the flask application
    Args:
        - app: the flask application's object
    """
    load_dotenv()
    app = create_app()
    mongo = db_connet(app)
    app.mongo = mongo

    initiate_routes(app)
    run_app(app)


if __name__ == "__main__":
    initiate_flask(create_app())
    