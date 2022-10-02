from bson.objectid import ObjectId


def get_all(mongo, collection):
    '''
    Fetches all data from the collection in the database
    mongo (Object): pyMongo object of the database
    collection (String): collection name
    '''
    if type(collection) != str:
        str(collection)

    return mongo.db[collection].find()


def get_one(mongo, collection, id):
    '''
    Fetches one document from the collection in the database
    mongo (Object): pyMongo object of the database
    collection (String): collection name
    id (string): The id of the document
    '''
    if type(collection) != str:
        str(collection)

    if type(id) != str:
        str(id)
    print('test: ', mongo.db[collection].find({'_id': ObjectId(id)}))

    return mongo.db[collection].find({'_id': ObjectId(id)})


def post_task(mongo, collection, new_doc):
    '''
    Posts an entry in a collection in the datbase
    mongo (Object): pyMongo object of the database
    collection (String): collection name
    new_doc (Dict): The entry data (new document)
    '''
    if type(collection) != str:
        str(collection)
    mongo.db[collection].insert_one(new_doc)
    

def delete_task(mongo, collection, id):
    '''
    Updates the value of a document in a collection in the datbase
    mongo (Object): pyMongo object of the database
    collection (String): collection name
    id (string): The id of the document
    '''
    if type(collection) != str:
        str(collection)

    if type(id) != str:
        str(id)

    mongo.db[collection].delete_one({'_id': ObjectId(id)})


def update_task(mongo, collection, title, done, id): # insted title and done you can pass new_doc
    '''
    Updates the value of a document in a collection in the datbase
    mongo (Object): pyMongo object of the database
    collection (String): collection name
    new_doc (Dict): The new document
    id (string): The id of the document
    '''
    if type(collection) != str:
        str(collection)

    if type(id) != str:
        str(id)
    
    mongo.db[collection].update_one(
        {'_id': ObjectId(id)}, 
        {'$set': {'title': title, 'done': done}}
        )