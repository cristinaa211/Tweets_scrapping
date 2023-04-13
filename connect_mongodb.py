import pymongo 

def connect_client():
    return pymongo.MongoClient("mongodb+srv://cristina211:passw0rd@cluster0.x5mxh5d.mongodb.net/test")


def insert_data_mongodb(database_name = 'tweets_wsc', collection_name = 'tweets_m', document_to_insert = {}):
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


if __name__ == '__main__':
    class Solution:
        def addBinary(self, a: str, b: str) -> str:
            lena, lenb = len(a), len(b)
            if a[0] == '0' and lena > 1 and b[0] == '0' and lenb > 1: 
                return False 
            if a.isdigit() and b.isdigit():
                if lena >= 1 and lena <= 1e4 and lenb  >=1 and lenb <= 1e4:
                    result = ''
                    extr = 0
                    a = a[::-1]
                    b = b[::-1]
                    for pos in range(max(lena, lenb)):
                        try:
                            res = int(a[pos]) + int(b[pos])+ extr
                        except :
                            try: 
                                res = int(a[pos]) + extr
                            except:
                                res = int(b[pos]) + extr
                        if res == 2:
                            result += '0'
                            extr = 1
                        elif res == 3:
                            result += '1'
                            extr = 1
                        elif res == 1:
                            result += '1'
                            extr = 0
                    if extr == 1:
                        result += '1'
                else: 
                    return False
            return result[::-1]     
        
    sol = Solution()
    binary = sol.addBinary('0', '0')
    binary