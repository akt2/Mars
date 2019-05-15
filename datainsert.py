import pymongo
from mar

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db=client.marsd
collection = db.marsc

db.collection.insert_one