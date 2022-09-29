from flask import Flask
import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()


template_dir = os.path.join(os.path.dirname(__name__), "templates")
app = Flask(__name__, template_folder=template_dir)
app.secret_key = "super secret key"


# Connect to the db
mongodb_host = os.getenv('MONGO_HOST')
client = MongoClient(mongodb_host)
db = client.todo
tasks_collection = db.tasks


# Views and blueprints


# Third party middilewares
