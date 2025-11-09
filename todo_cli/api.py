from fastapi import FastAPI
from pydantic import BaseModel
from .todo import *
from fastapi import HTTPException
from typing import Optional

app = FastAPI()

class TaskCreateRequest(BaseModel):
    description:str
    status:str

class TaskUpdateRequest(BaseModel):
    task_id:int
    description:Optional[str]
    status:Optional[str]


#Whenever a user sends some input through a POST request, it first goes to app.post("/tasks"). Then, FastAPI routes the request to the corresponding function create_task_api(task_req). The task_req parameter is linked to the Pydantic model TaskCreateRequest, which validates and converts the user’s input data. Once the data is successfully validated, the function executes using the validated values.

@app.post("/tasks",status_code=201)
def create_task_api(task_req : TaskCreateRequest):  #task_req is a parameter of the function — it represents the data that comes from the user (client) when someone sends a POST request to /tasks.
    """
    Create new task
    """
    task_list=load_tasks_from_file()
    next_id=get_next_task_id(task_list)
    try:
        new_task=create_task(next_id,task_req.description, task_req.status)
        add_task(task_list,new_task)
        print("Task created!!!")

    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))
    return new_task

@app.get("/tasks",status_code=200)
def get_task_api():
    """
    Get all tasks
    """
    task_list=load_tasks_from_file()
    return task_list

@app.get("/tasks/{task_id}", status_code=200)
def get_task_by_id(task_id: int):
    """
    Get a task by its ID
    """
    task_list = load_tasks_from_file()
    for task in task_list:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found") 
    

@app.put("/tasks",status_code=200)
def update_task_api(task_req:TaskUpdateRequest):
    """
    Update the task
    """
    task_list=load_tasks_from_file()
    data=task_req.dict(exclude_unset=True)
    task_id=data.pop("task_id")
    new_data=data
    if not update_task(task_list, task_id, new_data):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message":"Task updated", "task_id":task_id, "updated fields":new_data}
    
@app.delete("/tasks/{task_id}", status_code=200)
def delete_task_api(task_id:int):
    """
    Delete a task by its ID
    """
    task_list = load_tasks_from_file()
    for task in task_list:
        if task["id"] == task_id:
            task_list.remove(task)
            save_tasks_to_file(task_list)
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks",status_code=204)
def delete_all_tasks_api():
    """
    Delete all tasks
    """
    save_tasks_to_file([])
    return {"message": "All tasks deleted"}

