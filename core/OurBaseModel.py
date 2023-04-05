from pydantic import BaseModel

# We override Basemodel with our own because SQLALchemy does not return a dictonary by default
class OurBaseModel(BaseModel):
    class Config():
        orm_mode = True