# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from pydantic import BaseModel

from mylib.bot import search

app = FastAPI()

class Wiki(BaseModel):
    name: str
    sentences: int = 1

@app.post("/wiki")
async def search_story(wiki: Wiki):
    result = search(name=wiki.name,sentences = wiki.sentences)
    payload = {"wikipage": result}
    json_compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/")
async def root():
    return {"message": "Hello Functions"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}


if __name__ == '__main__':
    uvicorn.run(app, port=8082, host='0.0.0.0')