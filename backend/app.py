import os
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()
#client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


