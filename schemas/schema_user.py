'''
Esquemas Pydantic para el modelo User
'''
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    '''Esquema base para los usuarios'''
    rol_id: int
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    direccion: str
    correo_electronico: str
    numero_telefono: str
    estatus: bool = True

class UserCreate(UserBase):
    '''Esquema para crear un nuevo usuario'''
    contrasena: str

class UserUpdate(BaseModel):
    '''Esquema para actualizar un usuario existente (todos los campos opcionales)'''
    rol_id: Optional[int] = None
    nombre: Optional[str] = None
    primer_apellido: Optional[str] = None
    segundo_apellido: Optional[str] = None
    direccion: Optional[str] = None
    correo_electronico: Optional[str] = None
    numero_telefono: Optional[str] = None
    contrasena: Optional[str] = None
    estatus: Optional[bool] = None

class User(UserBase):
    '''Esquema para representar un usuario en la base de datos'''
    model_config = ConfigDict(from_attributes=True)
    id: int
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None

class UserLogin(BaseModel):
    '''Clase para realizar el login por numero o correo'''
    numero_telefono: Optional[str] = None
    correo_electronico: Optional[str] = None
    contrasena: str