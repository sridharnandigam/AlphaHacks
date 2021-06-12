from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

import json
import requests

#Get Brand embedding data and query
BRAND_EMB_DIR = 'C:\Sridhar\AlphaHacks\AlphHacks\AlphaHacks\brand_embeddings'


#Test Data
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

#Test stats
companyStats = [
    {
        "name": "Coke",
        "rating": 434,
        "articles": [
            {
                "article_title": "a title",
                "description": "a desc",
                "link": "https://whatever.wow",
                "image_link": "https://hi.jpg"
            },
        ],
    },
    {
        "name": "Oreos",
        "rating": 4343,
        "articles": [
            {
                "article_title": "another title",
                "description": "another desc",
                "link": "https://anotherwow.wow",
                "image_link": "https://anotherhi.jpg"
            },
        ],
    },
]

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

@app.get('/stats/{company}')
def getStats(company):
    for brand in companyStats:
        if brand['name'] == company:
            return brand['articles']