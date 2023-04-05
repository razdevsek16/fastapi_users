from sqlalchemy import Column, String, Integer, DateTime
from app.database import Base

class TrackM(Base):
    __tablename__ = 'trackLog'
    id = Column(Integer, primary_key=True, index = True)    # primary key
    start = Column(DateTime)                                # start tracking
    end = Column(DateTime)                                  # end tracking
    userId = Column(Integer)                                # userId
    trackType = Column(Integer)                             # tracking type (foreing key WorkType)
    
class TrackTypeM(Base):
    __tablename__ ='trackType'
    id = Column(Integer, primary_key=True, index = True)    # primary key
    type = Column(String)                                   # tracking type (work, lunch, private, business, paid-leaf, leaf, other..)
    maxPeriod = Column(Integer)                             # max tracking period