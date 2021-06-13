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

def query(target_brand_name, top_n=10):
    dict_kb = get_dict()

    target_brand_emb = np.array(dict_kb[target_brand_name])

    dict_brand_name_emb_distance = dict()
    for candidate_brand_name, candidate_emb in dict_kb.items():

        if candidate_brand_name.encode("ascii", "ignore").decode() == target_brand_name.encode("ascii", "ignore").decode():
            continue

        emb_dist = np.linalg.norm(target_brand_emb - np.array(candidate_emb))
        dict_brand_name_emb_distance[candidate_brand_name] = emb_dist

    sorted_dict = sorted(dict_brand_name_emb_distance.items(), key=operator.itemgetter(1))

    if top_n:
        sorted_dict = sorted_dict[: top_n]

    return sorted_dict
