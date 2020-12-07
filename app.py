from fastapi import FastAPI 
from pydantic import BaseModel

# import requests

app = FastAPI()

# class Employees(BaseModel):
#     name: str
#     time: str
#     date: str
#     day: str


@app.get('/')
def index():
    return {"message":"hello world"}