from typing import Optional
from pydantic import BaseModel
from pydantic import ConfigDict
from datetime import datetime, date

class ReporteBase(BaseModel):
    pass

class ReporteUpdate(BaseModel):
    pass

class ClienteVehiculo(BaseModel):
    cliente_id: int
    cliente_nombre: str
    vehiculo_id: int
    vehiculo_placa: str
    vehiculo_marca: str
    vehiculo_modelo: str
    vehiculo_color: str

class ServicioInfo(BaseModel):
    servicio_id: int
    servicio_nombre: str
    servicio_costo: float

class UsuarioInfo(BaseModel):
    usuario_id: int
    usuario_nombre: str

class Reporte(ReporteBase):
    id_servicio_vehiculo: int
    cliente_vehiculo: ClienteVehiculo
    servicio: ServicioInfo
    operativo: UsuarioInfo
    cajero: UsuarioInfo
    descuento: Optional[float] = 0
    total: float
    fecha_servicio: date
    hora_servicio: str
    
    class Config:
        orm_mode = True

class ReporteCreate(BaseModel):
    id_servicio_vehiculo: int
    descuento: float = 0

class ReporteResponse(BaseModel):
    success: bool
    data: Optional[Reporte] = None
    message: Optional[str] = None
    
    class Config:
        orm_mode = True
