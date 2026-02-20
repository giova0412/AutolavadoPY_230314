'''
Esquemas Pydantic para el modelo AutoServicio
'''
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class Auto_ServicioBase(BaseModel):
    '''Esquema base para los registros de auto-servicio'''
    auto_id: int
    cajero_id: int
    operador_id: int
    servicio_id: int
    fecha: datetime
    estatus: str = "Programando"
    estado: bool = True

class Auto_ServicioCreate(Auto_ServicioBase):
    '''Esquema para crear un nuevo registro de auto-servicio'''
    pass

class Auto_ServicioUpdate(BaseModel):
    '''Esquema para actualizar un auto-servicio existente (todos los campos opcionales)'''
    auto_id: Optional[int] = None
    cajero_id: Optional[int] = None
    operador_id: Optional[int] = None
    servicio_id: Optional[int] = None
    fecha: Optional[datetime] = None
    estatus: Optional[str] = None
    estado: Optional[bool] = None

class Auto_Servicio(Auto_ServicioBase):
    '''Esquema para representar un auto-servicio en la base de datos'''
    model_config = ConfigDict(from_attributes=True)
    id: int
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None