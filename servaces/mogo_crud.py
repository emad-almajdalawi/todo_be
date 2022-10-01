
def get_all(mongo, collection):
    '''
    Fetches all data from the collection in the database
    mongo (Object): pyMongo object of the database
    collection (String): collection name
    '''
    return list(mongo.db.collection.find({},{'_id':0}))

def post_task(mongo, collection, obj):
    '''
    Posts an entry in a collection in the datbase
    mongo (Object): pyMongo object of the database
    collection (String): collection name
    obj (Dict): The entry data
    '''
    return