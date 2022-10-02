from flask import (
    jsonify,
    request,
    redirect,
    url_for
)
from servaces.mogo_crud import get_all, post_task

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
            return jsonify(tasks)
            # return jsonify(message='Success', status=200), 200
        except:
            print('Importing from dattbase failed!')
            return 'Importing from dattbase failed!'


    @app.route('/<int:id>')
    def delete_task(app, mongo, id):
        pass


    @app.route('/<int:id>')
    def update_task(app, mongo, id):
        pass