from email import message
import json
from flask import jsonify, request
from bson import json_util
from services.mogo_crud import get_data, post_task, delete_task, update_task


def todo_routes(app):
    """
    Initiats all routes for the todo files

    Args:
        -app: the flask application's object
    """
    @app.route('/', methods=['GET'])
    def servive():
        """
        Creat the routes for the todo page to test if the server works

        Return:
            - JSON message of success
        """
        return jsonify(message='Success', status=200), 200


    @app.route('/tasks.json', methods = ['GET'])
    def get_todo_tasks():
        """
        Show all tasks

        Return:
            - Tasks data as Json
        """
        if request.method == 'GET':
            tasks = get_data(app.mongo, 'tasks', None)

            return json.loads(json_util.dumps(tasks))

        else:
            return jsonify(message='Method not allowed!', status=500), 500

    @app.route('/task/<id>.json', methods = ['GET'])
    def get_task_details(id=None):
        """
        Show task's details

        Args:
            - id: the id of the task to show its details

        Return:
            - Task's details as Json
        """
        if request.method == 'GET':
            if (id):
                task =  get_data(app.mongo, 'tasks', id)
                return json.loads(json_util.dumps(task))

        else:
            return jsonify(message='Method not allowed!', status=500), 500


    @app.route('/task/add', methods = ['POST'])
    def todo_add_task():
        """
        Add new task
        """
        title = request.form.get('title') #or requeist.args.get , or requist.json.get_json
        done_text = request.form.get('done')
        if type(done_text) == str:
            if done_text in ['True', 'true', 1]:
                done = True
            elif done_text in ['false', 'False', 0]:
                done = False
            
        new_doc = {'title': title, 'done': done}
        post_task(app.mongo, 'tasks', new_doc)

        return jsonify(message='Success', status='201'), 201



    @app.route('/task/delete/<id>', methods = ['POST'])
    def todo_delete_task(id):
        """
        Calls the CRUD methods to delete a task

        Args:
            - id: the id of the task to show its details
        """
        delete_task(app.mongo, 'tasks', id)

        return jsonify(message='Success', status='202'), 202



    @app.route('/task/update/<id>', methods = ['POST'])
    def todo_update_task(id):
        """
        Calls the CRUD methods to update the value of a task

        Args:
            - id: the id of the task to show its details
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

        return jsonify(message='Success', status='201'), 201

