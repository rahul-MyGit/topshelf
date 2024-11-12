from pydantic import BaseModel, Field
import uuid
from datetime import datetime

class UserCreateModel(BaseModel):

    firstname : str = Field(max_length=50)
    lastnname: str = Field(max_langth=40)
    username: str = Field(max_length=30)
    email: str = Field(max_length=50)
    password: str = Field( min_length=6)

    model_config= {
        'json_schema_extra': {
            "example": {
                "firstname": "rahul",
                "lastname": "gujjar",
                "username": "rahulgujjar",
                "email": "rahul@gmail.com",
                "password": "rahul123"
            }
        }
    }


class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    firstname: str
    lastname: str
    email: str
    password: str = Field(exclude=True)
    isverified: bool
    created_at: datetime
    updated_at: datetime

class UserLoginModel(BaseModel):
    email: str = Field(max_length=30)
    password: str = Field(min_length=6)