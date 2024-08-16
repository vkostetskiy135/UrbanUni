from fastapi import APIRouter
from Module17.HW2024_03_05.app.schemas import CreateUser, UpdateUser
router = APIRouter(prefix='/user', tags=['user'])

@router.get('/')
async def all_users():
    pass

@router.get('/user_id')
async def user_by_id():
    pass

@router.post('/create')
async def create_user(task : CreateUser):
    pass

@router.put('/update')
async def update_user(task :UpdateUser):
    pass

@router.delete('/delete')
async def delete_user():
    pass