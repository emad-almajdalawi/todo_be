from crypt import methods
from flask import (
    jsonify,
    request,
    redirect,
)
from servaces.mogo_crud import get_all, post_task

def landing_routes(app, mongo):
    @app.route("/", methods=["GET"])
    def main():
        # tasks = get_all(mongo, 'tasks')
        tasks = list(mongo.db.tasks.find({},{'_id':0}))
        return jsonify(tasks)

    @app.route("/", methods=['POST'])
    def main_post():
        # post_task(mongo, 'tasks')
        mongo.save_file()
        return redirect()
