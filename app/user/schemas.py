from core.OurBaseModel import OurBaseModel

class User(OurBaseModel):
    name : str
    username : str
    email : str
    password : str