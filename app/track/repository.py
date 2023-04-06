from typing import List, Optional
from fastapi import Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.database import get_db
from .models import TrackM, TrackTypeM
from .schemas import TrackTypeS
from app.user.repository import getUserById


class TrackTypeR:
    
    def __init__(self, user=None):
        self.user = user
    
    def getTrackType(self, id: int, response: Response, db: Session = Depends(get_db)):
        type = db.query(TrackTypeM).filter(TrackTypeM.id == id).first()
        print(type)
        if not type:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Type with the id {id} is not ")
        return self.parseToSchema(type,getUserById(type.userIns,response,db).name,getUserById(type.userUpd,response,db).name)

    def getAllTrackTypes(self, response: Response, db: Session= Depends(get_db)) -> List[TrackTypeS]:
        types = db.query(TrackTypeM).all()
        if types is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data found")
        return [self.parseToSchema(t,getUserById(t.userIns,response,db).name,getUserById(t.userUpd,response,db).name) for t in types]
    
    def createTrackType(self, request: TrackTypeS, db: Session = Depends(get_db)):
        new_trackType = TrackTypeM(type=request.type,
                                   maxPeriod=request.maxPeriod,
                                   userIns=request.userIns,
                                   dateIns=request.dateIns,
                                   userUpd=request.userUpd,
                                   dateUpd=request.dateUpd)
        db.add(new_trackType)
        db.commit()
        db.refresh(new_trackType)
        return new_trackType
    
    def deleteTrackType(self, id: int, db: Session = Depends(get_db)):
        tracktype = db.query(TrackTypeM).filter(TrackTypeM.id == id)
        if not tracktype.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Track type with the id {id} is not available")
        tracktype.delete(synchronize_session=False)
        db.commit()
        return f"Track type with id {id} was deleted"
    
    def parseToSchema(self, data: TrackTypeM, userInsName: str, userUpdName: str) -> TrackTypeS:
        return TrackTypeS(id=data.id,
                          type=data.type,
                          maxPeriod=data.maxPeriod,
                          userIns=data.userIns,
                          userInsName=userInsName,
                          dateIns=data.dateIns,
                          userUpd=data.userUpd,
                          userUpdName=userUpdName,
                          dateUpd=data.dateUpd)
    
class TrackR:
    def __init__(self, user=None):
        self.user = user
    
    