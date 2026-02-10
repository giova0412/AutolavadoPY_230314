from pydantic import BaseModel
from typing import Optional

class ClienteBase(BaseModel):
    nombre: str
    apellidoPaterno: str
    apellidoMaterno: str
    telefono: str
    direction: str
    email: str
    password: str
    status: Optional[bool] = True

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    apellidoPaterno: Optional[str] = None
    apellidoMaterno: Optional[str] = None
    telefono: Optional[str] = None
    direction: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    status: Optional[bool] = None

class Cliente(ClienteBase):
    id: int

    class Config:
        from_attributes = True