from sqlalchemy.orm import Session
import models.model_movimiento_inventario
import schemas.schema_movimiento_inventario

def get_movimiento(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.model_movimiento_inventario.MovimientoInventario).offset(skip).limit(limit).all()

def get_movimiento_by_id(db: Session, movimiento_id: int):
    return db.query(models.model_movimiento_inventario.MovimientoInventario).filter(
        models.model_movimiento_inventario.MovimientoInventario.Id == movimiento_id
    ).first()

def get_movimientos_by_producto(db: Session, producto_id: int):
    return db.query(models.model_movimiento_inventario.MovimientoInventario).filter(
        models.model_movimiento_inventario.MovimientoInventario.producto_Id == producto_id
    ).all()

def create_movimiento(db: Session, movimiento: schemas.schema_movimiento_inventario.MovimientoInventarioCreate):
    db_movimiento = models.model_movimiento_inventario.MovimientoInventario(
        producto_Id = movimiento.producto_Id,
        tipo_movimiento = movimiento.tipo_movimiento,
        cantidad = movimiento.cantidad,
        fecha_movimiento = movimiento.fecha_movimiento,
        usuario_Id = movimiento.usuario_Id
    )
    db.add(db_movimiento)
    db.commit()
    db.refresh(db_movimiento)
    return db_movimiento

def delete_movimiento(db: Session, id: int):
    db_movimiento = db.query(models.model_movimiento_inventario.MovimientoInventario).filter(
        models.model_movimiento_inventario.MovimientoInventario.Id == id
    ).first()
    if db_movimiento:
        db.delete(db_movimiento)
        db.commit()
    return db_movimiento
