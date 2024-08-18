from fastapi import APIRouter, Depends, HTTPException, status
from Module17.HW2024_03_06_part_2.app.schemas import CreateUser, UpdateUser, UserResponse, TaskResponse
from sqlalchemy.orm import Session
from Module17.HW2024_03_06_part_2.app.backend.db_depends import get_db
from typing import Annotated, List
from Module17.HW2024_03_06_part_2.app.models.user import User
from Module17.HW2024_03_06_part_2.app.models.task import Task
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix='/user', tags=['user'])


@router.get('/', response_model=List[UserResponse])
async def all_users(db: Annotated[Session, Depends(get_db)]):
    all_users = db.scalars(select(User)).all()
    return [UserResponse.model_validate(user) for user in all_users]


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int) -> dict:
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    return user


@router.get('/user_id/tasks', response_model=List[TaskResponse])
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    tasks_by_user = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    if tasks_by_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No tasks by user {user_id}')
    return [TaskResponse.model_validate(task) for task in tasks_by_user]


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user : CreateUser) -> dict:
    db.execute(insert(User).values(
        username=create_user.username,
        first_name=create_user.first_name,
        last_name=create_user.last_name,
        age=create_user.age,
        slug=slugify(create_user.username),
    ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user : UpdateUser) -> dict:
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

    db.execute(update(User).where(User.id == user_id).values(
        first_name=update_user.first_name,
        last_name=update_user.last_name,
        age=update_user.age,
    ))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful'}


@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):

    user = db.scalar(select(User).where(User.id == user_id))

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

    db.execute(delete(User).where(User.id == user_id))
    db.execute(delete(Task).where(Task.user_id == user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User successfully deleted'}