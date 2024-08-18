from fastapi import FastAPI
from Module17.HW2024_03_06_part_2.app.routers import task, user


app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)