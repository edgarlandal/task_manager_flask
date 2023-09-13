import requests

URL = "http://127.0.0.1:5000/tasks"

def create_task(summary, description):
    task_data = {
        "summary" : summary,
        "description" : description
    }

    response = requests.post(URL, json=task_data)

    if response.status_code == 204:
        print("Task created successfully.")
    else:
        print("Task creation failed")

if __name__ == "__main__":
    print("Create a new task: ")
    summary = input("Summary: ")
    description = input("Description: ")

    create_task(summary, description)