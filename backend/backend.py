from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
foodType = [
    {
        "name": "Drinks",
        "brands": ["orange juice", "coffee", "milk"]
    },
    {
        "name": "Cheese",
        "brands": ["American", "Cheddar", "mozarella"]   
    },
    {
        "name": "fruit",
        "brands": ["apple", "banana", "peach"]
    },
]
companyStats = []

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome To Sustainabrands"}

@app.get('/competitors/{name}')
def getCompetitors(name):
    for food in foodType:
        if food['name'] == name:
            return food['brands']
    return {"error": "Brands for specified food does not exist"}

# @app.get('/stats/{company}')  WIP
# def getStats(name):
#     for food in foodType:
#         if food['name'] == name:
#             return food