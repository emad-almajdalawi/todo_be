from flask import Flask
import os
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from routes.landing_routes import landing_routes


load_dotenv()


def create_app():
    """
    Description

    Args:
        - arg1: test test
        - arg2: test test

    Return:
        - return
    """
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KYE")
    return app


def db_connet(app):
    app.config["MONGO_URI"] = os.getenv('MONGO_HOST')
    mongo = PyMongo(app)
    return mongo


def run_app(app):
    app.run(debug = True)

def initiate_routes(app):
    landing_routes(app)


def initiate_flask(app):
    app = create_app()
    mongo = db_connet(app)
    app.mongo = mongo

    initiate_routes(app)
    run_app(app)


if __name__ == "__main__":
    initiate_flask(create_app())
    
