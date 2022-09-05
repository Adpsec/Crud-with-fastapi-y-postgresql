from ast import Str
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
    
class UserId(BaseModel):
    int: int