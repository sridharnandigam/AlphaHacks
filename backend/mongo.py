import pymongo

client = pymongo.MongoClient('localhost', 27017)

db = client['branddb']

list_of_db = client.list_database_names()
  
print(client.list_database_names())