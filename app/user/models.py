from sqlalchemy import Column, String, Integer
from app.database import Base

class UserM(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String)
    lastName = Column(String)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)
