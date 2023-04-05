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

@router.get('/{id}', status_code=status.HTTP_200_OK,response_model=TrackTypeS)
def getTrackType(id: int,response: Response, db: Session = Depends(get_db)):
    repository = TrackTypeR()
    return repository.getTrackType(id=id,response=response,db=db)