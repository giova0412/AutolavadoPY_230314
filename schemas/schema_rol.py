'''
Esquemas Pydantic para el modelo Rol
'''
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class RolBase(BaseModel):
    '''Esquema base para los roles'''
    nombre_rol: str
    estado: bool = True

class RolCreate(RolBase):
    '''Esquema para crear un nuevo rol'''
    pass

class RolUpdate(BaseModel):
    '''Esquema para actualizar un rol existente (todos los campos opcionales)'''
    nombre_rol: Optional[str] = None
    estado: Optional[bool] = None

class Rol(RolBase):
    '''Esquema para representar un rol en la base de datos'''
    model_config = ConfigDict(from_attributes=True)
    id: int
    fecha_registro: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None