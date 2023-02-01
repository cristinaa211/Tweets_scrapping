import pymongo 

def insert_data_mongodb(database_name = 'tweets_wsc', collection_name = 'tweets_m', document_to_insert = {}):
    client = pymongo.MongoClient("mongodb+srv://cristina211:passw0rd@cluster0.x5mxh5d.mongodb.net/test")
    db = client[database_name]
    collection = db[collection_name]
    collection.insert_one(document_to_insert)
    client.close()

