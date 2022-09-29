
def get_all(mongo, collection):
    '''
    Fetches all data from the collection in the database
    mongo: pyMongo object of the database
    collection: collection name
    '''
    return list(mongo.db.collection.find({},{'_id':0}))

def post_task():
    '''
    
    '''
    return