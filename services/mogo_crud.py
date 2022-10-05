from bson.objectid import ObjectId


def get_data(mongo, collection, id=None):
    """
    Fetches all data from the collection in the database, or get the details if the id is geven

    Args:
        - mongo (Object): pyMongo object of the database
        - collection (String): collection name

    Return:
        - All tasks
    """
    if type(collection) != str:
        str(collection)

    if id:
        if type(id) != str:
            str(id)

        return mongo.db[collection].find({'_id': ObjectId(id)})

    return mongo.db[collection].find()


def post_task(mongo, collection, new_doc):
    """
    Posts an entry in a collection in the datbase

    Args:
        - mongo (Object): pyMongo object of the database
        - collection (String): collection name
        - new_doc (Dict): The entry data (new document)
    """
    if type(collection) != str:
        str(collection)
    mongo.db[collection].insert_one(new_doc)
    

def update_task(mongo, collection, new_title, id): # insted title and done you can pass new_doc
    """
    Updates the title of a document in a collection in the datbase
    
    Args:
        - mongo (Object): pyMongo object of the database
        - collection (String): collection name
        - new_doc (Dict): The new document
        - id (string): The id of the document
    """
    if type(collection) != str:
        str(collection)

    if type(id) != str:
        str(id)

    mongo.db[collection].update_one({'_id': ObjectId(id)}, {'$set': {'title': new_title}})


def delete_task(mongo, collection, id):
    """
    Delete a document in a collection in the datbase

    Args:
        - mongo (Object): pyMongo object of the database
        - collection (String): collection name
        - id (string): The id of the document
    """
    if type(collection) != str:
        str(collection)

    if type(id) != str:
        str(id)

    mongo.db[collection].delete_one({'_id': ObjectId(id)})


def delete_all(mongo, collection):
    """
    Delete all documents in a collection in the datbase

    Args:
        - mongo (Object): pyMongo object of the database
        - collection (String): collection name
    """
    if type(collection) != str:
        str(collection)
    
    mongo.db[collection].delete_many({})


def task_done(mongo, collection, new_done, id):
    """
    Updates the (done value) of a document in a collection in the datbase
    
    Args:
        - mongo (Object): pyMongo object of the database
        - collection (String): collection name
        - new_doc (Dict): The new document
        - id (string): The id of the document
    """
    if type(collection) != str:
        str(collection)

    if type(id) != str:
        str(id)

    mongo.db[collection].update_one({'_id': ObjectId(id)}, {'$set': {'done': new_done}})


def all_tasks_done(mongo, collection, is_done):
    """
    Updates the (done value) of all documents in a collection in the datbase to be true (done)
    
    Args:
        - mongo (Object): pyMongo object of the database
        - collection (String): collection name
    """
    if type(collection) != str:
        str(collection)

    mongo.db[collection].update_many({}, {'$set': {'done': is_done}})


def delete_done(mongo, collection):
    """
    Delete all done tsks

    Args:
        - mongo (Object): pyMongo object of the database
        - collection (String): collection name
    """
    if type(collection) != str:
        str(collection)
    
    mongo.db[collection].delete_many({'done': True})