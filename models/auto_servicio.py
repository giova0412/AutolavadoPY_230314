'''Este archivo define el modelo de usuarios en la base de datos'''
from sqlalchemy import Column, Integer, String, Boolean,DateTime,Enum,Date,ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    '''Modelo para la tabla de usuarios'''
    __tablename__ = "tbc_usuarios"
    id = Column(Integer, primary_key=True, index=True)
    Rol_id = Column(Integer, ForeignKey("tbc_roles.id"))  # Llave foránea a la tabla de roles
    nombre = Column(String(50))
    apellidoPaterno = Column(String(50))
    apellidoMaterno = Column(String(50))
    password = Column(String(100), nullable=False)
    Rol_id = Column(Integer, nullable=False)