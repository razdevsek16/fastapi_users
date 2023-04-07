from typing import List, Optional
from datetime import datetime
from fastapi import Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.database import get_db
from .models import TrackM, TrackTypeM
from .schemas import TrackTypeS, TrackS
from app.user.repository import getUserById


class TrackTypeR:
    
    def __init__(self, user=None):
        self.user = user
    
    def getTrackType(self, id: int, response: Response, db: Session = Depends(get_db)):
        type = db.query(TrackTypeM).filter(TrackTypeM.id == id).first()
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
    
    
    def createTrack(self, track: TrackS, db: Session = Depends(get_db)):
        self.endPreviousTrack(track.userId, track.start, db)
        new_track = TrackM(start=track.start,
                           #end=track.end,
                           userId=track.userId,
                           trackType=track.trackTypeId,
                           userIns=track.userIns,
                           dateIns=track.dateIns,
                           userUpd=track.userUpd,
                           dateUpd=track.dateUpd)
        db.add(new_track)
        db.commit()
        db.refresh(new_track)
        return new_track
    
    def updateUser(self, id, data: TrackS, db: Session = Depends(get_db)):
        track = db.query(TrackM).filter(TrackM.id == id)
        if not track.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Track with the id {id} is not found")
        track.update(data)
        db.commit()
        return "Updated track"
    
    def endPreviousTrack(self, userId, endDate: datetime, db: Session = Depends(get_db)):
        track = db.query(TrackM).filter(TrackM.userId == userId).where(TrackM.end == None)
        if track.count() > 1:
            raise HTTPException(status_code=status.HTTP_300_MULTIPLE_CHOICES,
                            detail=f"To many open tracks with user {userId}!")
        elif track.count() == 0:
            return "No tracks to update"
        track.update({TrackM.end: endDate},synchronize_session = False)
        db.commit()
        return "Track updated"
        
    def getAllTracks(self, response: Response, userId, db: Session= Depends(get_db)) -> List[TrackS]:
        types = []
        if userId != None:
            print(userId)
            types = db.query(TrackM).where(TrackM.userId == userId).all()
        else:
            types = db.query(TrackM).all()
        if types is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data found")
        return [self.parseToSchema(t) for t in types]
    
    
    def parseToSchema(self, data: TrackM) -> TrackS:
        fullname = ""
        userInsName= ""
        userUpdName =""
        trackTypeName = ""
        return TrackS(id=data.id,
                      userId=data.userId,
                      userName=fullname,
                      start=data.start,
                      end=data.end,
                      trackTypeId=data.trackType,
                      trackType=trackTypeName,
                      userIns=data.userIns,
                      userInsName=userInsName,
                      dateIns=data.dateIns,
                      userUpd=data.userUpd,
                      userUpdName=userUpdName,
                      dateUpd=data.dateUpd)