
import string


def get_all(mongo, collection):
    '''
    Fetches all data from the collection in the database
    mongo (Object): pyMongo object of the database
    collection (String): collection name
    '''
    if type(collection) != string:
        str(collection)
    return list(mongo.db[collection].find({},{'_id':0}))

def post_task(mongo, collection, new_doc):
    '''
    Posts an entry in a collection in the datbase
    mongo (Object): pyMongo object of the database
    collection (String): collection name
    doc (Dict): The entry data
    '''
    if type(collection) != string:
        str(collection)
    mongo.db[collection].insert_one(new_doc)
    return 201