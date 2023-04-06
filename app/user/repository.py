from fastapi import Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.database import get_db
from app.user.models import UserM
from app.user.schemas import UserS
from app.hashing import Hash

def get_all(db: Session = Depends(get_db)):
    users = db.query(UserM).all()
    return users

def getUserById(id, response: Response, db: Session = Depends(get_db)):
    user = db.query(UserM).filter(UserM.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return getSchema(user)

def createUser(request: UserS, db: Session = Depends(get_db)):
    new_user = UserM(firstName=request.firstName,
                     lastName=request.lastName,
                     name=request.name, 
                     username=request.username, 
                     email=request.email, 
                     password=Hash.bcrypt(request.password))  # type: ignore
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def updateUser(id, request: UserS, db: Session = Depends(get_db)):
    user = db.query(UserM).filter(UserM.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    user.update(request)
    db.commit()
    return "Updated"

def deleteUser(id, db: Session = Depends(get_db)):
    user = db.query(UserM).filter(UserM.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    user.delete(synchronize_session=False)
    db.commit()
    return "User has been deleted"

def get_test(db: Session = Depends(get_db)):
    print(dir(db))
    # users = db.execute(text('select * from users')).fetchall()
    # for row in users:
    #     print(row)
    return "ok"

def getSchema(user: UserM):
    return UserS(id=user.id,
                 firstName=user.firstName,
                 lastName=user.lastName,
                 name=user.name,
                 username=user.username,
                 email=user.email,
                 password=user.password)