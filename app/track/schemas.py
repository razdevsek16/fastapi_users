from core.OurBaseModel import OurBaseModel
from typing import Optional, List
from datetime import datetime

class TrackS(OurBaseModel):
    id: int
    userId: int
    userName: Optional[str]
    start: datetime
    end: datetime
    trackTypeId: int
    trackType: Optional[str]
    
class TrackTypeS(OurBaseModel):
    id: Optional[int]
    type: Optional[str]
    maxPeriod: Optional[int]
