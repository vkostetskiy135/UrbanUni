from fastapi import FastAPI, status, Body, HTTPException, Path
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
def get_users() -> List[User]:
    return users


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
