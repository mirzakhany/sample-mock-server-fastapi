from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from data import create_mock_data, tasks, get_task, update_task, add_task, remove_task, check_user


class Task(BaseModel):
    id: Optional[str] = None
    title: str
    sprint: str
    status: str
    estimate: str
    assignee: str


class LoginReq(BaseModel):
    email: str
    password: str


create_mock_data()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_uuid}")
def get_task_item(task_uuid: str):
    return get_task(task_uuid)


@app.post("/tasks")
def add_task_item(task_item: Task):
    return add_task(task_item)


@app.put("/tasks/{task_uuid}")
def update_task_item(task_uuid: str, task_item: Task):
    return update_task(task_uuid, task_item)


@app.delete("/tasks/{tasks_uuid}")
def delete_task_item(task_uuid: str):
    return remove_task(task_uuid)


@app.post("/auth/login")
def login(login_req: LoginReq):
    return check_user(login_req)
