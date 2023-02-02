import pymongo 

def insert_data_mongodb(database_name = 'tweets_wsc', collection_name = 'tweets_m', document_to_insert = {}):
    client = pymongo.MongoClient("mongodb+srv://cristina211:passw0rd@cluster0.x5mxh5d.mongodb.net/test")
    db = client[database_name]
    collection = db[collection_name]
    if len(document_to_insert) > 1:
        collection.insert_many(document_to_insert)
    else:
        collection.insert_one(document_to_insert)
    client.close()

