from fastapi import FastAPI
from pydantic import BaseModel
from .todo import *
from fastapi import HTTPException

app = FastAPI()

class TaskCreateRequest(BaseModel):
    description:str
    status:str

#Whenever a user sends some input through a POST request, it first goes to app.post("/tasks"). Then, FastAPI routes the request to the corresponding function create_task_api(task_req). The task_req parameter is linked to the Pydantic model TaskCreateRequest, which validates and converts the user’s input data. Once the data is successfully validated, the function executes using the validated values.

@app.post("/tasks",status_code=201)
def create_task_api(task_req : TaskCreateRequest):  #task_req is a parameter of the function — it represents the data that comes from the user (client) when someone sends a POST request to /tasks.
    task_list=load_tasks_from_file()
    next_id=get_next_task_id(task_list)
    try:
        new_task=create_task(next_id,task_req.description, task_req.status)
        add_task(task_list,new_task)
        print("Task created!!!")

    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))
    
    return new_task