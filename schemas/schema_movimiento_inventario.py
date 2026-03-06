from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from pydantic import ConfigDict
from enum import Enum

class TipoMovimientoEnum(str, Enum):
    entrada = "entrada"
    salida = "salida"

class MovimientoInventarioBase(BaseModel):
    producto_Id: int
    tipo_movimiento: TipoMovimientoEnum
    cantidad: int
    fecha_movimiento: datetime
    usuario_Id: int

class MovimientoInventarioCreate(MovimientoInventarioBase):
    pass

class MovimientoInventarioUpdate(MovimientoInventarioBase):
    pass

class MovimientoInventario(MovimientoInventarioBase):
    Id: int
    class Config:
        orm_mode = True
