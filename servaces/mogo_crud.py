
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

    return mongo.db[collection].find({'_id': {'$oid': id}})


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
    
    return 201


def update_task(mongo, collection, new_doc, id):
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
        {'_id': {'$oid': id}}, 
        {'$set': {'title': f'{new_doc}.title', 'done': f'{new_doc}.done'}}
        )

    return 201


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

    mongo.db[collection].delte_one({'_id': {'$oid': id}})

    return 201