from flask import Flask
import os
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from routes.landing_routes import landing_routes


load_dotenv()


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KYE")
    return app


def db_connet(app):
    app.config["MONGO_URI"] = os.getenv('MONGO_HOST')
    mongo = PyMongo(app)
    return mongo


def run_app(app):
    app.run(debug = True)

def initiate_routes(app, mongo):
    landing_routes(app, mongo)


if __name__ == "__main__":
    app = create_app()
    mongo = db_connet(app)
    
    initiate_routes(app, mongo)
    run_app(app)
