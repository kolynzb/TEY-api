from fastapi import FastAPI
from todo import todo_router

# Instantiate fast API
app = FastAPI()




@app.get("/")
async def say_hello() -> dict: 
       return {"message": "Welcome to the East Yard"}

app.include_router(todo_router)