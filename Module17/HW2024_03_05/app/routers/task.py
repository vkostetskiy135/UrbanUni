from fastapi import APIRouter
from Module17.HW2024_03_05.app.schemas import CreateTask, UpdateTask
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
