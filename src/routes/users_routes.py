from multiprocessing import synchronize
from typing import List
from fastapi import APIRouter, Depends 
from database.db import get_db 
from schemas.user_schema import ShowUser, User, UserId
from sqlalchemy.orm import Session
from models.user_model import User

router = APIRouter(
    prefix="/api",
    tags=["Users"]
)

# Routes

@router.get("/")
def index():
    return {"message": "Here is FastAPI"}

@router.get("/users", response_model=List(ShowUser))
def get_users(db: Session = Depends(get_db)):
    data = db.query(User).all()
    
    print(data)
    return {}

@router.get("user/{id}", response_model=ShowUser)
def get_user(user_id: id, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        return {"message": "User not found"}
    else:
        return user 

@router.post("/user")
def create_user(user: User, db: Session = Depends(get_db)):
    usuario = user.dcit()
    new_user = User(
        username = User["username"],
        password = User["password"],
        nombre = User["nombre"],
        apellido=  User["apellido"],
        direccion=  User["direccion"],
        telefono= User["telefono"],
        email =  User["email"]
    )
    
    db.add(new_user)
    db.commit()
    db.refresh()
    

@router.patch("/user/{id}")
def update_user(user_id: int, updateUser: User, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id)
    if not user.first():
        return {"message": "User not found"}
    user.update(updateUser.dict(exclude_unser = True))
    db.commit()
    return {"message": "User updated"}
    

@router.post("/user/{id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id)
    if not user.first():
        return {"message": "User not found"}
    user.delete(synchronize_session = False)
    db.commit()
    return {"message": "User deleted"}
