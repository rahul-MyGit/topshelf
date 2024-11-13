from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from src.auth.schemas import UserCreateModel, UserLoginModel, UserModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from src.auth.service import UserService
from src.auth.utils import verify_hash, generate_token
from datetime import timedelta

user_router = APIRouter()
user_service = UserService()

REFRESH_TOKEN_EXP = 2

@user_router.post('/signup', status_code=status.HTTP_201_CREATED)
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
    user_email = user_data.email

    isUser = await user_service.get_user_by_email(user_email, session)
    if isUser is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User doesnt exists, try signup')
    
    if verify_hash(user_data.password, isUser.password):
        access_token = generate_token(
            user_data = {
                'email': isUser.email,
                'user_uid': str(isUser.uid)
            }
        )

        refresh_token = generate_token(
            user_data={
                'email': isUser.email,
                'user_uid': str(isUser.uid)
            },
            refresh=True,
            expiry=timedelta(days=REFRESH_TOKEN_EXP)

        )

        return JSONResponse(
            content={
                'message': 'Login successfull',
                'access-token': access_token,
                'refresh-token': refresh_token,
                'user': {
                    'email': isUser.email,
                    'uid': str(isUser.uid)
                }
            }
        )
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='Details are wrong')

