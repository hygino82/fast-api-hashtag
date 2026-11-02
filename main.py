from fastapi import FastAPI
import os
from dotenv import load_dotenv

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}