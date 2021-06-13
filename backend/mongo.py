import os
import json
import pymongo

BRAND_EMB_DIR = r"C:/Sridhar/AlphaHacks/AlphHacks/AlphaHacks/brand_embeddings/embeddings.json"

client = pymongo.MongoClient('localhost', 27017)

db = client['branddb']

list_of_db = client.list_database_names()
  
Collection = db["data"]
  
# Loading or Opening the json file
with open(BRAND_EMB_DIR) as file:
    file_data = json.load(file)
      
#print(file_data['A._L._Simpkin_%26_Co._Ltd'])

new_dict = {key.replace('.', '#'): file_data[key] for key in list(file_data)}

# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else inser_one is used
if isinstance(new_dict, list):
    Collection.insert_many(new_dict, check_keys =False)  
else:
    Collection.insert_one(new_dict, bypass_document_validation = True)