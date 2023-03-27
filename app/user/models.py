from sqlalchemy import Column, String, Integer
from app.database import Base

# add Base Database to class User
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)
