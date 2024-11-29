from fastapi import Request, status
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from .utils import decode_token
from fastapi.exceptions import HTTPException

class TokenBearer(HTTPBearer):
    
    def __init__(self, auto_error=True):
        super().__init__(auto_error=auto_error)


    async def __call__(self, request : Request) -> HTTPAuthorizationCredentials | None :
        creds = await super().__call__(request)

        token = creds.credentials

        token_data = decode_token(token)


        if not self.isVerifyToken:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Invalid token')
        
        if token_data['refresh']:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='please provide access token')

        return token_data 
    
    async def isVerifyToken(self , token : str) -> bool:

        tokens = decode_token(token)

        return True if tokens is not None else None
    


class AccessTokenBearer(HTTPBearer):
    pass

class RefreshTokenBearer(HTTPBearer):
    pass