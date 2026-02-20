'''
Esquemas Pydantic para el modelo Service (Servicios)
'''
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class ServicioBase(BaseModel):
    '''Esquema base para Servicio'''
    nombre: str
    descripcion: str
    costo: float
    duracion: int
    estado: bool = True

class ServicioCreate(ServicioBase):
    '''Esquema para crear un nuevo servicio'''
    pass

class ServicioUpdate(BaseModel):
    '''Esquema para actualizar un servicio existente (todos los campos opcionales)'''
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    costo: Optional[float] = None
    duracion: Optional[int] = None
    estado: Optional[bool] = None

class Servicio(ServicioBase):
    '''Esquema para representar un servicio en la base de datos'''
    model_config = ConfigDict(from_attributes=True)
    id: int
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None