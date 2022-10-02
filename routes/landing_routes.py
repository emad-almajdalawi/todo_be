from flask import (
    request,
    redirect,
    url_for
)
from servaces.mogo_crud import get_all, get_one, post_task,delete_task, update_task
import json
from bson import json_util


def landing_routes(app, mongo):
    @app.route('/', methods=['GET', 'POST'])
    def landing():
        if request.method == 'POST':
            title = request.form.get('title') #or requeist.args.get , or requist.json.get_json
            done = request.form.get('done')
            new_doc = {'title': title, 'done': done}
            try:
                post_task(mongo, 'tasks', new_doc)
            except:
                print('Posting data error!') 
                return 'Posting data error!'

            return redirect(url_for('landing'))

        try:
            tasks = get_all(mongo, 'tasks')
            return json.loads(json_util.dumps(tasks))
            # return jsonify(message='Success', status=200), 200
        except:
            print('Importing from dattbase failed!')
            return 'Importing from dattbase failed!'

    @app.route('/<int:id>', methods = ['GET'])
    def landing_task_details():
        get_one(mongo, 'tasks', id)

    @app.route('/delete/<int:id>', methods = ['POST'])
    def landing_delete_task():
        delete_task(mongo, 'tasks', id)


    @app.route('/update/<int:id>', methods = ['POST'])
    def landing_update_task():
        new_doc = {}
        update_task(mongo, 'tasks', new_doc, id)
