from fastapi import APIRouter
from Module17.HW2024_03_06.app.schemas import CreateTask, UpdateTask
from sqlalchemy.orm import Session
from Module17.HW2024_03_06.app.backend.db_depends import get_db
from typing import Annotated
from Module17.HW2024_03_06.app.models import *
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix='/task', tags=['task'])

@router.get('/')
async def all_tasks():
    pass


@router.get('/task_id')
async def task_by_id():
    pass


@router.post('/create')
async def create_task(task: CreateTask):
    pass


@router.put('/update')
async def update_task(taskL :UpdateTask):
    pass


@router.delete('/delete')
async def delete_task():
    pass
