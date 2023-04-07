from sqlalchemy import Column, String, Integer, DateTime
from app.database import Base

class TrackM(Base):
    __tablename__ = 'track'
    id = Column(Integer, primary_key=True, index = True)    # primary key
    start = Column(DateTime)                                # start tracking
    end = Column(DateTime, nullable=True)                   # end tracking
    userId = Column(Integer)                                # userId
    trackType = Column(Integer)                             # tracking type (foreing key WorkType)
    userIns = Column(Integer)                                # User data inserted
    dateIns = Column(DateTime)                              # Date data inserted
    userUpd = Column(Integer)                                # User data updated
    dateUpd = Column(DateTime)                              # Date data updated
    
class TrackTypeM(Base):
    __tablename__ ='trackType'
    id = Column(Integer, primary_key=True, index = True)    # primary key
    type = Column(String)                                   # tracking type (work, lunch, private, business, paid-leaf, leaf, other..)
    maxPeriod = Column(Integer)                             # max tracking period
    userIns = Column(Integer)                                # User data inserted
    dateIns = Column(DateTime)                              # Date data inserted
    userUpd = Column(Integer)                                # User data updated
    dateUpd = Column(DateTime)                              # Date data updated