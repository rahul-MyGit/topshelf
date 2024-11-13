from .schemas import UserCreateModel, UserLoginModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .models import User
from .utils import generate_hash


class UserService:

    async def get_user_by_email(self, email: str, session : AsyncSession):
        statement = select(User).where(email == User.email)
        res = await session.exec(statement)
        user = res.first()

        return user if user is not None else None
    

    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):
        user_data_in_dict = user_data.model_dump()

        try:
            new_user = User(
                **user_data_in_dict
            )

            new_user.password = generate_hash(user_data_in_dict['password'])

            session.add(new_user)
            await session.commit()
            return new_user

        except Exception as e:
            print(f'Error while creating the User', (e))
            return None


    async def exist_user(self, email: str, session: AsyncSession):
        user = await self.get_user_by_email(email, session)

        if user is None:
            return False
        else:
            return True
        

    