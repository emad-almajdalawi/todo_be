from flask import Flask
import os
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from flask import jsonify
from servaces.mogo_crud import get_all


template_dir = os.path.join(os.path.dirname(__name__), "templates")
app = Flask(__name__, template_folder=template_dir)
app.secret_key = '1234'
app.config["MONGO_URI"] = 'mongodb+srv://mongo_practicing:YSAZE9fx2W1ztrWr@cluster0.2ad7r7v.mongodb.net/todo?retryWrites=true&w=majority'
mongo = PyMongo(app)

print(list(mongo.db.tasks.find({},{'_id':0})))
