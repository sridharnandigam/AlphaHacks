import os
from dotenv import load_dotenv

import json
import pymongo

load_dotenv()

BRAND_EMB_DIR = os.environ.get("EMBEDDING_PATH")

client = pymongo.MongoClient('localhost', 27017)

db = client['embeddb']

list_of_db = client.list_database_names()
  
Collection = db["data"]
  
# Loading or Opening the json file
with open(BRAND_EMB_DIR) as file:
    file_data = json.load(file)

dict_list = []
for key, value in file_data.items():
    temp_dict = {"brand" : key.replace('.', '#'), "emb": value}
    #print(temp_dict["brand"])
    dict_list.append(temp_dict)

Collection.insert_many(dict_list)
