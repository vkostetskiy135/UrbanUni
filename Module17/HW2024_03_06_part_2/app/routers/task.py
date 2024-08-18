from fastapi import APIRouter, Depends, HTTPException, status
from Module17.HW2024_03_06_part_2.app.schemas import CreateTask, UpdateTask, TaskResponse
from sqlalchemy.orm import Session
from Module17.HW2024_03_06_part_2.app.backend.db_depends import get_db
from typing import Annotated, List
from Module17.HW2024_03_06_part_2.app.models.user import User
from Module17.HW2024_03_06_part_2.app.models.task import Task
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix='/task', tags=['task'])

@router.get('/', response_model=List[TaskResponse])
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    all_tasks = db.scalars(select(Task)).all()
    return [TaskResponse.model_validate(user) for user in all_tasks]

@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')
    return task 


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], user_id: int, create_task : CreateTask) -> dict:
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

    new_task = Task(
        title=create_task.title,
        content=create_task.content,
        priority=create_task.priority,
        user_id=user_id,
        slug=slugify(create_task.title)
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful',
    }


@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, update_task : UpdateTask) -> dict:
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')

    db.execute(update(Task).where(Task.id == task_id).values(
        title=update_task.title,
        content=update_task.content,
        priority=update_task.priority,
        completed=update_task.completed,
    ))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful'}


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):

    task = db.scalar(select(Task).where(Task.id == task_id))

    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')

    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task successfully deleted'}
