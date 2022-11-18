from fastapi import APIRouter,Path
from model import Todo,Item as TodoItem 

todo_router = APIRouter()

todos_schemas = []

@todo_router.get("/todo")
async def get_todo()-> dict:
    return {"todos":todos_schemas}

@todo_router.post("/todo")
async def add_todo(todo:Todo)-> dict:
    todos_schemas.append(todo)
    return {"message":"Todo added successfully","todos":todos_schemas}

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data:TodoItem,todo_id:int=Path(...,title="The ID of the todo to retrieve"))-> dict:
    for todo in todos_schemas: 
            if todo.id == todo_id:
                todo.item = todo_data.item
                return { 
                    "todo": todo  
                     }   
            return {        
                "message": "Todo with supplied ID doesn't exist."   
                 }

# Path parameters
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id:int=Path(...,title="The ID of the todo to retrieve"))-> dict:
        for todo in todos_schemas: 
            if todo.id == todo_id:
                return { 
                    "todo": todo  
                     }   
            return {        
                "message": "Todo with supplied ID doesn't exist."   
                 }


@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:   
    for index in range(len(todos_schemas)):       
        todo = todos_schemas[index]       
        if todo.id == todo_id:            
            todos_schemas.pop(index)           
            return {              
                "message": "Todo deleted successfully."           
                }   
            return {       
                "message": "Todo with supplied ID doesn't exist."   
                }

@todo_router.delete("/todo")
async def delete_all_todo() -> dict:   
    todos_schemas.clear()   
    return {       "message": "Todos deleted successfully."}

    # pg 106