from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from src.auth.schemas import UserCreateModel, UserLoginModel, UserModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from src.auth.service import UserService

user_router = APIRouter()
user_service = UserService()

@user_router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UserModel)
async def user_signup( user_data: UserCreateModel, session : AsyncSession = Depends(get_session)):
    user_email = user_data.email

    isuser = await user_service.exist_user(user_email, session)
    if isuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='User with email already exists')
    else:
        new_user = await user_service.create_user(user_data, session)

    
    return new_user

@user_router.post('/login', status_code=status.HTTP_200_OK)
async def user_signin(user_data: UserLoginModel, session : AsyncSession = Depends(get_session)):
    pass



