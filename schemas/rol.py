from pydantic import BaseModel
from typing import Optional

class RolBase(BaseModel):
    nombreRol: str
    estado: Optional[bool] = None

class RolCreate(RolBase):
    pass

class RolUpdate(BaseModel):
    nombreRol: Optional[str] = None
    estado: Optional[bool] = None

class Rol(RolBase):
    id: int

    class Config:
        from_attributes = True