from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.oauth2 import get_current_user

from .repository import TrackTypeR
from .schemas import TrackS, TrackTypeS

router = APIRouter(
    prefix='/track',
    tags= ['Track']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def createTrackType(request: TrackTypeS, db: Session = Depends(get_db)):
    repository = TrackTypeR()
    return repository.createTrackType(request=request,db=db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deleteTrackType(id: int, db:Session=Depends(get_db)):
    respository = TrackTypeR()
    return respository.deleteTrackType(id, db)

@router.get('/{id}', status_code=status.HTTP_200_OK,response_model=TrackTypeS)
def getTrackType(id: int,response: Response, db: Session = Depends(get_db)):
    repository = TrackTypeR()
    return repository.getTrackType(id=id,response=response,db=db)

@router.get('/all/', status_code=status.HTTP_200_OK,response_model=List[TrackTypeS])
def getAllTrackTypes(response: Response, db: Session = Depends(get_db)):
    repository = TrackTypeR()
    return repository.getAllTrackTypes(response=response,db=db)