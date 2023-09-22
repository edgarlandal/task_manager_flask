from flask import Flask, request
from server.app.database import task

app = Flask(__name__)


@app.get("/tasks")
def get_all_task():
    task_list = task.scan()
    out = {"ok": True, "tasks": task_list}
    return out


@app.post("/tasks")
def create_task():
    task_data = request.json
    task.insert(task_data)
    return "", 204


@app.get("/tasks/<int:pk>")
def get_single_task(pk: int):
    status_code = 200

    single_task = task.select_by_id(pk)
    if not single_task:
        status_code = 404

    out = {"ok": True, "task": single_task}
    return out, status_code


@app.put("/tasks/<int:pk>")
def update_task(pk: int):
    task_data = request.json
    task.update(task_data, pk)
    return "", 204


@app.delete("/tasks/<int:pk>")
def delete_task(pk: int):
    task.delete(pk)
    return "", 204
