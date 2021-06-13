import json
import pymongo
import operator
import numpy as np

from pymongo import MongoClient
from bson import ObjectId

from functools import reduce

client = pymongo.MongoClient('localhost', 27017)

db = client.embeddb
collection = db.data

docs = list(collection.find())

test_key = "Kellogg's"

def get_dict():
    keys = reduce( lambda all_keys, rec_keys: all_keys | set(rec_keys), map(lambda d: d.keys(), collection.find()), set())

    temp_dict = {}
    for key in keys:
        #print("Load data for key: {}".format(key))
        temp_dict[key.replace('#', '.')] = collection.distinct(key)

    #print("Loaded in {} rows\n".format(len(temp_dict.keys())))
    other_key = "CJ Group"
    print(len(temp_dict[other_key]))
    print(len(temp_dict[test_key]))
    return temp_dict

def query(target_brand_name, top_n=10):
    #dict_kb = get_dict()
    
    target_brand_emb = np.array(collection.find_one({"brand":target_brand_name})['emb'])

    #print(collection.find_one({"brand":target_brand_name})['emb'])
    #return -1

    dict_brand_name_emb_distance = dict()
    for doc in collection.find():
        #print(doc.keys())
        candidate_brand_name = doc["brand"]
        candidate_emb = doc["emb"]
        
        #print([type(item) for item in candidate_emb])

        if candidate_brand_name.encode("ascii", "ignore").decode() == target_brand_name.encode("ascii", "ignore").decode():
            continue

        print("Brand name: {}".format(candidate_brand_name))
        emb_dist = np.linalg.norm(target_brand_emb - np.array(candidate_emb))
        dict_brand_name_emb_distance[candidate_brand_name] = emb_dist

    sorted_dict = sorted(dict_brand_name_emb_distance.items(), key=operator.itemgetter(1))

    if top_n:
        sorted_dict = sorted_dict[: top_n]

    return sorted_dict

query(test_key)