from flask import Flask, jsonify
import os
from flask_pymongo import PyMongo
from dotenv import load_dotenv

from routes import initiate_routes


load_dotenv()


def create_app():
    template_dir = os.path.join(os.path.dirname(__name__), "templates")
    app = Flask(__name__, template_folder=template_dir)
    app.secret_key = os.getenv("SECRET_KYE")
    return app


def db_connet(app):
    app.config["MONGO_URI"] = os.getenv('MONGO_HOST')
    mongo = PyMongo(app)
    return mongo


def run_app(app):
    app.run(debug = True)


if __name__ == "__main__":
    app = create_app()
    mongo = db_connet(app)
    
    initiate_routes(app, mongo)
    run_app(app)
