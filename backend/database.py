from pydantic import BaseModel, Field, EmailStr
from bson.objectid import ObjectId
from typing import Optional, List
import motor.motor_asyncio

import query_db

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.branddb

collection = database.get_collection("data")

async def retrieve_brand(id: str) -> dict:
    brand = await collection.find_one({"_id": ObjectId(id)})

    similar_brands = brand_query.query(brand_name, kb_fpath= BRAND_EMB_DIR)
    print(similar_brands)

    return json.dumps(dict(lst))
    if student:
        return student_helper(student)
