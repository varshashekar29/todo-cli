import json
import os

def save_tasks_to_file(tasks, filename="tasks.json"):
    """
    Save a list of tasks to a JSON file.
    
    Args:
        tasks (list): List of task dictionaries to save
        filename (str): Name of the file to save to (default: tasks.json)
    """
    with open(filename, "w") as f:  # f is the file object
        json.dump(tasks, f, indent=2)  # indent=2 makes JSON readable
    

def load_tasks_from_file(filename="tasks.json"):
    try:
        with open(filename,"r") as f:
            tasks=json.load(f)
        return tasks
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading tasks {e}")
        return []
    


# Test the function
if __name__ == "__main__":
    # Create some test data
    test_tasks = [
        {"id": 1, "description": "Learn JSON", "status": "pending"},
        {"id": 2, "description": "Test storage", "status": "done"}
    ]
    
    # Save the tasks
    save_tasks_to_file(test_tasks)
    print("✅ Tasks saved to tasks.json!")
    print("📁 Check the file to see your data!")