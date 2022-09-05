from fastapi import APIRouter, Depends 
from database.db import get_db 
from schemas.user_schema import User, UserId
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

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    data = db.query(User).all()
    
    print(data)
    return {}

@router.get("users/{id}")
def get_user():
    pass

@router.post("/users")
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
    

@router.put("/users/{id}")
def update_user():
    pass

@router.post("/users/{id}")
def delete_user():
    pass