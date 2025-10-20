"""
Core TODO functionality for managing tasks.

This module provides functions to create, validate, and display tasks.
It serves as the business logic layer for the TODO CLI application.
"""

STATUS_TO_DO="To Do"
STATUS_IN_PROGRESS="In Progress"
STATUS_DONE="Done"

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

def display_tasks(tasks):
    """
Display a list of tasks in a formatted output.    
Args:
    tasks (list): List of task dictionaries to display
"""
    for task in tasks:
        print(f" {task['id']}. {task['description']} [{task['status']}] ")

if __name__=="__main__":
    task1=create_task(1,"Watch film",STATUS_DONE)
    task2=create_task(2,"Buy dress",STATUS_TO_DO)
    task3=create_task(3,"Learn coding",STATUS_IN_PROGRESS)

    task_list = [task1,task2,task3]
    display_tasks(task_list)