from .storage import load_tasks_from_file,save_tasks_to_file

"""
Core TODO functionality for managing tasks.

This module provides functions to create, validate, and display tasks.
It serves as the business logic layer for the TODO CLI application.
"""

STATUS_TO_DO="To Do"
STATUS_IN_PROGRESS="In Progress"
STATUS_DONE="Done"

def get_next_task_id(task_list):
    if not task_list:
        return 1
    else:
        for task in task_list:
            max_id=max(task["id"] for task in task_list)
        return max_id+1

def create_task(id, description, status):
    """
    Create a new task dictionary.    
    Args:
        id (int): Unique identifier for the task
        description (str): Description of the task
        status (str): Current status of the task    
    Returns:
        dict: Task dictionary containing id, description, and status
    """
    if not isinstance(id,int) or id<=0:
        raise ValueError("ID must be positive number")
    if not description or not description.strip():
        raise ValueError("Description cannot be empty")
    if status not in [STATUS_TO_DO,STATUS_IN_PROGRESS,STATUS_DONE]:
        raise ValueError(f"status must be one of: {STATUS_TO_DO,STATUS_IN_PROGRESS,STATUS_DONE}")
    task = {
        "id":id,
        "description":description,
        "status":status
        }      
    return task

def add_task(task_list, new_task):
    task_list.append(new_task)
    save_tasks_to_file(task_list)

def remove_task(task_list,task_id):
    for task in task_list:
        if task["id"]==task_id:
            task_list.remove(task)
            save_tasks_to_file(task_list)
            return True
    return False        

def update_task(task_list,task_id,new_data):
    for task in task_list:
        if task["id"]==task_id:
            task.update(new_data)
            save_tasks_to_file(task_list)
            return True
    return False 
    

def display_tasks(tasks):
    """
Display a list of tasks in a formatted output.    
Args:
    tasks (list): List of task dictionaries to display
"""
    for task in tasks:
        print(f" {task['id']}. {task['description']} [{task['status']}] ")

if __name__=="__main__":
    task_list = load_tasks_from_file()
    next_id=get_next_task_id(task_list)
    new_task=create_task(next_id,"Dancing", STATUS_TO_DO)
    add_task(task_list, new_task)
    display_tasks(task_list)
    