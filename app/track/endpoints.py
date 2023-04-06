from typing import List
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

@router.post('/',status_code=status.HTTP_201_CREATED)
def createTrack(request: TrackS, db: Session = Depends(get_db)):
    repository = TrackR()
    return repository.createTrack(request,db)