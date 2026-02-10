from pydantic import BaseModel
from typing import Optional

class ServiceBase(BaseModel):
    precio: float
    status: Optional[bool] = True
    descripcion: Optional[str] = None
    nombreServicio: str
    UserID: int

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(BaseModel):
    precio: Optional[float] = None
    status: Optional[bool] = None
    descripcion: Optional[str] = None
    nombreServicio: Optional[str] = None
    UserID: Optional[int] = None

class Service(ServiceBase):
    id: int

    class Config:
        from_attributes = True