from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .schemas import User
from app.database import get_db
from . import repository
from app.auth.oauth2 import get_current_user
#from ..auth import oauth2

router = APIRouter(
    prefix='/user',
    tags= ['User']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def createUser(request: User, db: Session = Depends(get_db)):
    return repository.createUser(request,db)

@router.get('/', response_model=List[User])
def all(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return repository.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=User)
def getUserById(id, response: Response, db: Session = Depends(get_db)):
    return repository.getUserById(id, response, db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def updateUser(id, request: User, db: Session = Depends(get_db)):
    return repository.updateUser(id,request,db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deleteUser(id, db: Session = Depends(get_db)):
    return repository.deleteUser(id, db)

@router.get('test/')
def test(db: Session = Depends(get_db)):
    return repository.get_test(db)