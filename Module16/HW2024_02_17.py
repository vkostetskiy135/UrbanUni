from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def root() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def post_user(username: Annotated[str, Path(max_length=20, min_length=3, example='UserName', description='Enter username')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter your age', example=25)]) -> str:
    current_id = str(int(max(users, key=int))+1)
    users[current_id] = f'Имя: {username}, возраст: {age}'
    return f'User {current_id} is registered'

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(le=100, ge=1, description='Enter id', example=33)],
                      username: Annotated[str, Path(max_length=20, min_length=3, example='UserName', description='Enter username')],
                      age: Annotated[int, Path(le=120, ge=18, description='Enter your age', example=25)]) -> str:
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} has been updated'

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(le=100, ge=1, description='Enter id', example=33)]) -> str:
    del users[str(user_id)]
    return f'User {user_id} has been deleted'

