from flask import (
    jsonify,
    request,
    redirect,
    url_for
)
from servaces.mogo_crud import get_all, get_one, post_task,delete_task, update_task
import json
from bson import json_util


def landing_routes(app):
    @app.route('/', methods=['GET'])
    def landing():
        return jsonify(message='Success', status=200), 200


    @app.route('/tasks.json', methods = ['GET', 'POST'])
    @app.route('/task.json/<id>', methods = ['GET'])
    def landing_task_details(id=None):
        if request.method == 'GET':
            if (id):
                task =  get_one(app.mongo, 'tasks', id)
                return json.loads(json_util.dumps(task))
            else:
                tasks = get_all(app.mongo, 'tasks')
                return json.loads(json_util.dumps(tasks))
        else:
            title = request.form.get('title') #or requeist.args.get , or requist.json.get_json
            done_text = request.form.get('done')
            if type(done_text) == str:
                if done_text in ['True', 'true', 1]:
                    done = True
                elif done_text in ['false', 'False', 0]:
                    done = False
                
            new_doc = {'title': title, 'done': done}
            post_task(app.mongo, 'tasks', new_doc)
            return redirect(url_for('landing'))


    @app.route('/task.json/delete/<id>', methods = ['POST'])
    def landing_delete_task(id):
        delete_task(app.mongo, 'tasks', id)
        return redirect(url_for('landing'))



    @app.route('/task.json/update/<id>', methods = ['POST'])
    def landing_update_task(id):
        title = request.form.get('title') #or requeist.args.get , or requist.json.get_json
        done_text = request.form.get('done')
        if type(done_text) == str:
                if done_text in ['True', 'true', 1]:
                    done = True
                elif done_text in ['false', 'False', 0]:
                    done = False
                
        # new_doc = {'title': title, 'done': done}        
        update_task(app.mongo, 'tasks', title, done, id)
        return redirect(url_for('landing'))
