from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    first_name: str
    last_name: str
    age: int


class UpdateUser(BaseModel):
    first_name: str
    last_name: str
    age: int


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int


class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int
    completed: bool


class UserResponse(BaseModel):
    username: str
    first_name: str
    last_name: str
    age: int
    slug: str
    id: int

    model_config = {
        "from_attributes": True
    }


class TaskResponse(BaseModel):
    id: int
    title: str
    content: str
    priority: int
    completed: bool
    user_id: int
    slug: str

    model_config = {
        "from_attributes": True
    }