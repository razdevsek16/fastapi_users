
from pydantic import BaseModel

class User(BaseModel):
    name : str
    username : str
    email : str
    password : str
    class Config():
        orm_mode = True
        
class Login(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None