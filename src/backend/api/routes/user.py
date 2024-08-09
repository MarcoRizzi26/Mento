from fastapi import APIRouter
from api.classes.UserManager import User, UserManager

router = APIRouter()

@router.get('/{email}')
async def read_one(email: str):
    return UserManager.select(email)

@router.get('/')
async def read_all():
    return UserManager.select_all()

@router.post('/')
async def create(user: User):
    return UserManager().insert(user)

@router.put('/{email}')
async def update(email: str, user: User):
    return UserManager().update(email, user)

@router.delete('/{email}')
async def delete(email: str):
    return UserManager.delete(email)