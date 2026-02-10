from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    Rol_id: int
    nombre: str
    apellidoPaterno: str
    apellidoMaterno: str
    password: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    Rol_id: Optional[int] = None
    nombre: Optional[str] = None
    apellidoPaterno: Optional[str] = None
    apellidoMaterno: Optional[str] = None
    password: Optional[str] = None

class User(UserBase):
    id: int

    class Config:
        from_attributes = True