from core.OurBaseModel import OurBaseModel
from typing import Optional, List
from datetime import datetime

class TrackS(OurBaseModel):
    id: int
    userId: int
    userName: Optional[str]
    start: datetime
    end: Optional[datetime]
    trackTypeId: int
    trackType: Optional[str]
    userIns: int
    userInsName: Optional[str]
    dateIns: datetime
    userUpd: Optional[int]
    userUpdName: Optional[str]
    dateUpd: Optional[datetime]
    
class TrackTypeS(OurBaseModel):
    id: Optional[int]
    type: Optional[str]
    maxPeriod: Optional[int]
    userIns: int
    userInsName: Optional[str]
    dateIns: datetime
    userUpd: Optional[int]
    userUpdName: Optional[str]
    dateUpd: Optional[datetime]   
