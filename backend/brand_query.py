import operator
import codecs
import os
import json

def load_embeddings(kb_fpath):
    with open(kb_fpath) as fp:
        temp_dict = json.load(fp)
    return temp_dict

def query(target_brand_name, top_n=10, kb_fpath = None, dict_kb=None):

    #if type(target_brand_name) == str:
    #    target_brand_name = str(target_brand_name)

    if dict_kb is None:
        load_embeddings(target_brand_name)

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

    logger.debug("{}: {}".format(target_brand_name, sorted_dict))

    return sorted_dict

if __name__ == "__main__":
    BRAND_EMB_DIR = r"C:/Sridhar/AlphaHacks/AlphHacks/AlphaHacks/brand_embeddings/embeddings.json"
    assert os.path.isfile(BRAND_EMB_DIR)
    data_dict = load_embeddings(BRAND_EMB_DIR)
    print({k: data_dict[k] for k in list(data_dict)[:100]})