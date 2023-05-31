import pymongo 

def connect_client():
    return pymongo.MongoClient("")


def insert_data_mongodb(database_name = '', collection_name = '', document_to_insert = {}):
    client = connect_client()
    db = client[database_name]
    collection = db[collection_name]
    if len(document_to_insert) > 1:
        collection.insert_many(document_to_insert)
    else:
        collection.insert_one(document_to_insert)
    client.close()

def read_from_db(database_name, collection_name):
    client = connect_client()
    db = client[database_name]
    collection = db[collection_name]
    documents = collection.find({})
    documents_list = [document for document in documents]
    if len(documents_list) == 0 :
        print('There are no documents in collection {}.'.format(collection_name))
    else:
        print(f'There are {len(documents_list)} documents in this collection.')
    return documents_list

