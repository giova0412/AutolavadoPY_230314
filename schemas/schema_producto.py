from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from pydantic import ConfigDict

class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    categoria: str
    unidad_medida: str
    stock_actual: float
    stock_minimo: float
    precio: float
    fecha_registro: datetime
    fecha_actualizacion: datetime
    estado: bool

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class Producto(ProductoBase):
    Id: int
    class Config:
        orm_mode = True
