from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.orm import relationship
from config.db import Base

class Producto(Base):
    __tablename__ = "tbb_productos"

    Id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    descripcion = Column(String(500))
    categoria = Column(String(50))
    unidad_medida = Column(String(20))
    stock_actual = Column(Float, default=0)
    stock_minimo = Column(Float, default=0)
    precio = Column(Float)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)
    estado = Column(Boolean, default=True)

    movimientos = relationship("MovimientoInventario", back_populates="producto")
