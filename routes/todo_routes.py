import json
from flask import jsonify, request
from bson import json_util
from services.mogo_crud import delete_done, get_data, post_task, delete_task, task_done, update_task, delete_all, all_tasks_done


def serialize(data):
    ser_data = {}
    kyes = [ 'title', 'done']
    ser_data['id'] = str(data["_id"])
    for feild_key in kyes:
        ser_data[feild_key] = data[feild_key]

    return ser_data


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
        new_doc = request.get_json() #or requeist.args.get , or requist.form.get
        post_task(app.mongo, 'tasks', new_doc)
        serialized = serialize(new_doc)

        return jsonify(message='Success', status='201', data=serialized), 201,


    @app.route('/task/update/<id>', methods = ['POST'])
    def todo_update_task(id):
        """
        Calls the CRUD methods to update the title of a task

        Args:
            - id: the id of the task to show its details
        """
        req = request.get_json() #or requeist.args.get , or requist.form.get
        title = req['title']
                     
        update_task(app.mongo, 'tasks', title, id)

        updated_doc = list(get_data(app.mongo, 'tasks',id))[0]
        serialised = serialize(updated_doc)

        return jsonify(message = 'Success', status = '201', data = serialised), 201


    @app.route('/task/delete/<id>', methods = ['POST'])
    def todo_delete_task(id):
        """
        Calls the CRUD methods to delete a task

        Args:
            - id: the id of the task to show its details
        """
        deleted_doc = list(get_data(app.mongo, 'tasks',id))[0]
        serialised = serialize(deleted_doc)

        delete_task(app.mongo, 'tasks', id)

        return jsonify(message='Success', status='202', data= serialised), 202


    @app.route('/task/deleteall', methods = ['POST'])
    def todo_delete_all():
        """
        Calls the CRUD methods to delete all tasks
        """
        delete_all(app.mongo, 'tasks')

        return jsonify(message='Success', status='202'), 202


    @app.route('/task/done/<id>', methods = ['POST'])
    def todo_update_done(id):
        """
        Calls the CRUD methods to update the (done value) of a task

        Args:
            - id: the id of the task to show its details
        """
        req = request.get_json() #or requeist.args.get , or requist.form.get
        done = req['done']
                     
        task_done(app.mongo, 'tasks', done, id)

        updated_doc = list(get_data(app.mongo, 'tasks',id))[0]
        serialised = serialize(updated_doc)

        return jsonify(message = 'Success', status = '201', data = serialised), 201

    
    @app.route('/task/alldone/<is_done>', methods = ['POST'])
    def todo_update_all_done(is_done):
        """
        Calls the CRUD methods to update the (done value) of all tasks to be true (done)
        """
        if is_done in ['true', 'True']:
            is_done = True
        if is_done in ['false', 'False']:
            is_done = False
        all_tasks_done(app.mongo, 'tasks', is_done)

        return jsonify(message = 'Success', status = '201'), 201


    @app.route('/task/deletedone', methods = ['POST'])
    def todo_delete_done():
        """
        Calls the CRUD methods to delete done tasks
        """
        delete_done(app.mongo, 'tasks')

        return jsonify(message='Success', status='202'), 202

