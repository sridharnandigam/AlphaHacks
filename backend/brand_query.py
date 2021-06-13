import operator
import codecs
import os
import json
import numpy as np

from dotenv import load_dotenv

load_dotenv()
BRAND_EMB_DIR = os.environ.get("EMBEDDING_PATH")
other_key = "CJ Group"

def load_embeddings(kb_fpath = BRAND_EMB_DIR):
    with open(kb_fpath) as fp:
        temp_dict = json.load(fp)
    print(len(temp_dict[other_key]))
    return temp_dict

def query(target_brand_name, top_n=10, kb_fpath = BRAND_EMB_DIR, dict_kb=None):

    #if type(target_brand_name) == str:
    #    target_brand_name = str(target_brand_name)

    if dict_kb is None:
        dict_kb = load_embeddings(kb_fpath)

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

    #print("{}: {}".format(target_brand_name, sorted_dict))

    return sorted_dict

load_embeddings()