from typing import List, Optional
from datetime import datetime
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.oauth2 import get_current_user

from .repository import TrackTypeR, TrackR
from .schemas import TrackS, TrackTypeS

router = APIRouter(
    prefix='/track',
    tags= ['Track']
)
path_type = "/type"

#
#   Apies for TRACKTYPE entity
#

@router.post(path_type+'/', status_code=status.HTTP_201_CREATED)
def createTrackType(request: TrackTypeS, db: Session = Depends(get_db)):
    repository = TrackTypeR()
    return repository.createTrackType(request=request,db=db)

@router.delete(path_type+'/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deleteTrackType(id: int, db:Session=Depends(get_db)):
    respository = TrackTypeR()
    return respository.deleteTrackType(id, db)

@router.get(path_type+'/{id}', status_code=status.HTTP_200_OK,response_model=TrackTypeS)
def getTrackType(id: int,response: Response, db: Session = Depends(get_db)):
    repository = TrackTypeR()
    return repository.getTrackType(id=id,response=response,db=db)

@router.get(path_type+'/all/', status_code=status.HTTP_200_OK,response_model=List[TrackTypeS])
def getAllTrackTypes(response: Response, db: Session = Depends(get_db)):
    repository = TrackTypeR()
    return repository.getAllTrackTypes(response=response,db=db)

#
#   Apies for TRACK entity
#

@router.post('/start/',status_code=status.HTTP_201_CREATED)
def createTrack(request: TrackS, db: Session = Depends(get_db)):
    repository = TrackR()
    return repository.createTrack(request,db)

@router.post('/end/',status_code=status.HTTP_201_CREATED)
def createEndTrack(user: int, endDate: datetime, db: Session = Depends(get_db)):
    repository = TrackR()
    return repository.endPreviousTrack(user,endDate,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def updateTrack(id, request: TrackS, db: Session = Depends(get_db)):
    repository = TrackR()
    return repository.updateUser(id,request,db)

@router.get('/all/', status_code=status.HTTP_200_OK,response_model=List[TrackS])
def getAllTracks(response: Response, userId: Optional[int] = None, db: Session = Depends(get_db)):
    repository = TrackR()
    return repository.getAllTracks(response,userId,db)