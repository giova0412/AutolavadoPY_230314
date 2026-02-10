from pydantic import BaseModel
from typing import Optional

class AutoBase(BaseModel):
    modelo: str
    matriucla: str
    marca: str
    color: str
    status: Optional[bool] = True
    clienteID: int

class AutoCreate(AutoBase):
    pass

class AutoUpdate(BaseModel):
    modelo: Optional[str] = None
    matriucla: Optional[str] = None
    marca: Optional[str] = None
    color: Optional[str] = None
    status: Optional[bool] = None
    clienteID: Optional[int] = None

class Auto(AutoBase):
    id: int

    class Config:
        from_attributes = True