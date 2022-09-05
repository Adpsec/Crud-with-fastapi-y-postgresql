from ast import Str
import email
from email.policy import strict
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    #id: Optional[str]
    username: str
    password: str 
    nombre: str
    apellido: str 
    direccion: Optional[str] 
    telefono: str 
    email: str 
    creacion: datetime = datetime.now()
    
class UpdateUser(BaseModel):
    #id: Optional[str]
    username: str = None 
    password: str = None 
    nombre: str = None 
    apellido: str = None 
    direccion: str = None 
    telefono: str = None 
    email: str = None

class UserId(BaseModel):
    id: int
    
class ShowUser(BaseModel):
    username: str 
    email: str 
    class Config():
        orm_mode = True