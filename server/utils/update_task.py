import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/tasks"

def display_task(id):
    response = requests.get(URL + f"/{id}")

    if response.status_code == 200:
        pprint(response.json())
    else:
        print(f"No task with id = {id}")

def update_task(summary, description, is_active, id):
    task_data = {
        "summary" : summary,
        "description" : description,
        "is_active" : is_active
    }

    response = requests.put(f"{URL}/{id}", json=task_data)

    if response.status_code == 204:
        print("Task created successfully.")
    else:
        print("Task creation failed")

if __name__ == "__main__":
    id = int(input("Task id to update: "))

    print("Before update: ")
    display_task(id)

    print("New task values:")

    summary = input("Summary: ")
    description = input("Description: ")
    is_active = int(input("Is active?: "))

    update_task(summary, description, is_active, id)
    
    print("After update")
    display_task(id)


