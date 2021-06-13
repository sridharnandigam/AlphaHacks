import json
import pymongo

from pymongo import MongoClient

from functools import reduce

client = pymongo.MongoClient('localhost', 27017)

db = client.branddb
collection = db.data

docs = list(collection.find())

def get_dict():
    keys = reduce( lambda all_keys, rec_keys: all_keys | set(rec_keys), map(lambda d: d.keys(), collection.find()), set())

    temp_dict = {}
    for key in keys:
        print("Load data for key: {}".format(key))
        temp_dict[key] = collection.distinct(key)

    print("Loaded in {} rows\n".format(len(temp_dict.keys())))
