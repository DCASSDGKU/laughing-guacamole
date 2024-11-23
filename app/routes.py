from flask import (
    Flask,
    request
)
from app.database import task

app = Flask(__name__)



@app.get("/")
@app.get("/task")
def scan():
    out = {
        "task": task.scan(),
        "ok": True
    }
    return out

@app.get("/task/<int:pk>/")
def get_single_task(pk):
    single_task = task.select_by_id(pk)
    out = {
        "ok": True
    }
    if not single_task:
        out["ok"] = False
        out["mesage"] = "Task not found"
        return out, 404
    

@app.put("/task/<int:pk>/")
def update(pk):
    task_data = request.json
    task.update_by_id(task_data, pk)
    return "", 204

@app.delete("/task/<int:pk?")
def delete_task(pk):
    task.delete_by_id(pk)
    return "", 204

@app.post("/task")
def create_task():
    task_data = request.json
    task.insert(task_data)
    return "", 204
