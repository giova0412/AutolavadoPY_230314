'''
Esquemas Pydantic para el modelo Auto
'''
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class AutoBase(BaseModel):
    '''Esquema base para el modelo de auto'''
    usuario_id: int
    modelo: str
    placa: str
    serie: str
    color: str
    tipo: str
    anio: int
    estado: bool = True
    marca: str

class AutoCreate(AutoBase):
    '''Esquema para crear un nuevo auto'''
    pass

class AutoUpdate(BaseModel):
    '''Esquema para actualizar un auto existente (todos los campos opcionales)'''
    usuario_id: Optional[int] = None
    modelo: Optional[str] = None
    placa: Optional[str] = None
    serie: Optional[str] = None
    color: Optional[str] = None
    tipo: Optional[str] = None
    anio: Optional[int] = None
    estado: Optional[bool] = None
    marca: Optional[str] = None

class Auto(AutoBase):
    '''Esquema para representar un auto en la base de datos'''
    model_config = ConfigDict(from_attributes=True)
    id: int
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None