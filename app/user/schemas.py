from core.OurBaseModel import OurBaseModel
from typing import Optional

class UserS(OurBaseModel):
    id : Optional[int]
    firstName: str
    lastName: str
    name : str
    username : str
    email : str
    password : str