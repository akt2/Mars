import pymongo

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db=client.mars
collection = db.marsc

db.collection