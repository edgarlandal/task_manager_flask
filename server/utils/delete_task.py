import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/tasks"

def display_task(id):
    response = requests.get(URL + f"/{id}")

    if response.status_code == 200:
        pprint(response.json())
    else:
        print(f"No task with id = {id}")

def delete_task(id):
    response = requests.delete(URL + f"/{id}")

    if response.status_code == 204:
        print("Task deleted successfully.")
    else:
        print("Task not deleted")

if __name__ == "__main__":
    id = int(input("Task id to update: "))

    display_task(id)

    print(f"You sure you want to delete task with id = {id}?")
    res = input("[yes/no]: ")
    if(res == "yes"):
        delete_task(id)
    else:
        print("Task not deleted")


