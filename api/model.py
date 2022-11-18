from pydantic import BaseModel

class Item(BaseModel):
    item:str
    status:str
    # Example schema appaerance for redoc
    class Config:
        schema_extra = {
            "Example":{
                "id":1,
                "item":"Example schema!"
                }
        }

class Todo(BaseModel):
    id:int
    item:Item
