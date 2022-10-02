from flask import (
    jsonify,
    request,
    redirect,
    url_for
)
from servaces.mogo_crud import get_all, get_one, post_task,delete_task, update_task
import json
from bson import json_util


def load_routes(app):
    """
    Initiats all routes for the todo files
    Args:
        -app: the flask application's object
    """
    @app.route('/', methods=['GET'])
    def todo_servive():
        """
        Creats the route for the landing page to test if the server works
        Return:
            - JSON message of success
        """
        return jsonify(message='Success', status=200), 200


    @app.route('/tasks.json', methods = ['GET', 'POST'])
    @app.route('/task.json/<id>', methods = ['GET'])
    def todo_tasks_and_details(id=None):
        """
        Calls the CRUD methods to show all tasks, the deatails of each task, and to post new task
        Args:
            - id: the id of the task to show its details
        Return:
            - redirect to the landing page
        """
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

            return redirect(url_for('todo_servive'))


    @app.route('/task.json/delete/<id>', methods = ['POST'])
    def todo_delete_task(id):
        """
        Calls the CRUD methods to delete a task
        Args:
            - id: the id of the task to show its details
        Return:
            - redirect to the landing page
        """
        delete_task(app.mongo, 'tasks', id)
        return redirect(url_for('todo_servive'))



    @app.route('/task.json/update/<id>', methods = ['POST'])
    def todo_update_task(id):
        """
        Calls the CRUD methods to update the value of a task
        Args:
            - id: the id of the task to show its details
        Return:
            - redirect to the landing page
        """
        title = request.form.get('title') #or requeist.args.get , or requist.json.get_json
        done_text = request.form.get('done')
        if type(done_text) == str:
                if done_text in ['True', 'true', 1]:
                    done = True
                elif done_text in ['false', 'False', 0]:
                    done = False
                
        # new_doc = {'title': title, 'done': done}        
        update_task(app.mongo, 'tasks', title, done, id)
        
        return redirect(url_for('todo_servive'))
