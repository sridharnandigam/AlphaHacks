from fastapi import FastAPI, File, UploadFile
from typing import List

from starlette.responses import HTMLResponse

import os
import json
import requests

import brand_query

#Get Brand embedding data and query
BRAND_EMB_DIR = r"C:/Sridhar/AlphaHacks/AlphHacks/AlphaHacks/brand_embeddings/embeddings.json"
assert os.path.isfile(BRAND_EMB_DIR)


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
    content = """
    <body>
    <form action="/files/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    </body>
    """
    return HTMLResponse(content=content)


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
    return {"error": "Companies for specific food does not exist"}

def getSimilarBrands(brand_name):
    brand_name = "Cavalier Chocolate"
    similar_brands = brand_query.query(brand_name, kb_fpath= BRAND_EMB_DIR)
    print(similar_brands)

@app.post("/files/")
def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}
