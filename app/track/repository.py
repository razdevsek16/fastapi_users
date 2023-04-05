from fastapi import Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.database import get_db
from .models import TrackM, TrackTypeM
from .schemas import TrackTypeS


class TrackTypeR:
    
    def __init__(self, user=None):
        self.user = user
    
    def getTrackType(self, id: int, response: Response, db: Session = Depends(get_db)):
        type = db.query(TrackTypeM).filter(TrackTypeM.id == id).first()
        print(type)
        if not type:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Type with the id {id} is not ")
        return type

    def createTrackType(self, request: TrackTypeS, db: Session = Depends(get_db)):
        new_trackType = TrackTypeM(type=request.type,maxPeriod=request.maxPeriod)
        db.add(new_trackType)
        db.commit()
        db.refresh(new_trackType)
        return new_trackType
    
class TrackR:
    def __init__(self, user=None):
        self.user = user
    
    