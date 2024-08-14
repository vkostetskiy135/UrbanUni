from fastapi import FastAPI, status, Body, HTTPException, Path, Request
from pydantic import BaseModel
from typing import List, Annotated
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

users = []

templates = Jinja2Templates(directory="Module16/HW2024_02_22/templates")


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, 'users': users})

@app.get("/user/{user_id}")
def get_users(request: Request, user_id: int) -> HTMLResponse:
    user = None
    for u in users:
        if u.id == user_id:
            user = u
            break
    if not user:
        raise HTTPException(status_code=404, detail="User was not found")
    return templates.TemplateResponse("users.html", {"request": request, 'user': user})


@app.post("/user/{username}/{age}")
def post_user(username: str, age: int) -> User:
    if not users:
        current_id = 1
    else:
        current_id = users[-1].id + 1
    users.append(User(id=current_id, username=username, age=age))
    return users[-1]


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> User:
    for user in users:
        if user.id == user_id:
            user.username, user.age = username, age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> User:
    for i, user in enumerate(users, start=0):
        if user.id == user_id:
            return users.pop(i)
    raise HTTPException(status_code=404, detail="User was not found")