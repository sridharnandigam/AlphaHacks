import os
from fastapi import FastAPI, Body, HTTPException, status
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from database import retrieve_brand

router = APIRouter()

app = FastAPI()
app.include_router(router, tags = ["Brand"], prefix = "/brand")

@router.get("/{id}", response_description="Brands retrieved")
async def get_brands():
    brands = await retrieve_brand()
    if students:
        return {"data": brands,
                "code": 200,
                "message": "successfully called api"}
    return {"code": 200,
            "message": "Empty list returned"}


#client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


