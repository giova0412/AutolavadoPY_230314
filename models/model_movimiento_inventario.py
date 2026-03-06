from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class TipoMovimiento(str, enum.Enum):
    entrada = "entrada"
    salida = "salida"

class MovimientoInventario(Base):
    __tablename__ = "tbd_movimientos_inventario"

    Id = Column(Integer, primary_key=True, index=True)
    producto_Id = Column(Integer, ForeignKey("tbb_productos.Id"))
    tipo_movimiento = Column(Enum(TipoMovimiento))
    cantidad = Column(Integer)
    fecha_movimiento = Column(DateTime)
    usuario_Id = Column(Integer, ForeignKey("tbb_usuarios.Id"))

    producto = relationship("Producto", back_populates="movimientos")
