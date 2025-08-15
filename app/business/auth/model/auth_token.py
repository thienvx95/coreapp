
from pydantic import BaseModel
from typing import Optional

class AuthToken(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class AuthTokenData(BaseModel):
    username: Optional[str] = None
    
class AuthRefreshTokenRequest(BaseModel):
    refresh_token: str