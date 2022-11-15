from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    id:int
    name:str
    description:str
    price:int
    on_offer:bool

@app.get('/')
def index():
    return {"message":"Hello World?"}


@app.get('/greet/{name}')
def great_name(name):
    return {"message":f"Hello  {name}"}


@app.put('/item/{item_id}')
def update_item(item_id:int,item:Item):
    return {"name":Item.name,"description":Item.description}
