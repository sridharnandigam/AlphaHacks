import json
import pymongo

from pymongo import MongoClient

from functools import reduce

client = pymongo.MongoClient('localhost', 27017)

db = client.branddb
collection = db.data

docs = list(collection.find())

#print(docs[:2])
keys = reduce( lambda all_keys, rec_keys: all_keys | set(rec_keys), map(lambda d: d.keys(), collection.find()), set())

print(keys)
print(len(keys))
