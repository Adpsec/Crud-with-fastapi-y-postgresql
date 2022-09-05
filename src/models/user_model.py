from enum import unique
from tkinter import CASCADE
from traceback import format_exc
from database.db import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime 
from datetime import datetime 
from sqlalchemy.schema import ForeignKey 
from sqlalchemy.orm import relationship 


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    apellido = Column(String)
    username: Column(String, unique=True)
    password = Column(String)
    direccion = Column(String)
    telefono = Column(String)
    email = Column(String, unique=True)
    creacion = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    estado = Column(Boolean, default=False)
    venta = relationship("Ventas", backref="user", cascade="delete,merge")
    
class Ventas(Base):
    __tablename__ = "ventas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    ventas = Column(Integer)
    ventas_productos = Column(Integer)
    