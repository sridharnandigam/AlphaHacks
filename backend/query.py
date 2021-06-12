import operator
import codecs

def query(target_brand_name, top_n=10, kb_fpath=emb_save_fp, dict_kb=None):

    #if type(target_brand_name) == str:
    #    target_brand_name = str(target_brand_name)

    if dict_kb is None:
        with codecs.open(kb_fpath, encoding='utf-8') as fp:
            dict_kb = json.load(fp)

    target_brand_emb = np.array(dict_kb[target_brand_name])

    dict_brand_name_emb_distance = dict()
    for candidate_brand_name, candidate_emb in dict_kb.items():

        if candidate_brand_name == target_brand_name:
            continue

        emb_dist = np.linalg.norm(target_brand_emb - np.array(candidate_emb))
        dict_brand_name_emb_distance[candidate_brand_name] = emb_dist

    sorted_dict = sorted(dict_brand_name_emb_distance.items(), key=operator.itemgetter(1))

    if top_n:
        sorted_dict = sorted_dict[: top_n]

    logger.debug("{}: {}".format(target_brand_name, sorted_dict))

    return sorted_dict