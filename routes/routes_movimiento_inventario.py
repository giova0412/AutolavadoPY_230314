from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import config.db
import crud.crud_movimiento_inventario
import schemas.schema_movimiento_inventario
import models.model_movimiento_inventario
from typing import List
import auth

movimiento_inventario = APIRouter()

models.model_movimiento_inventario.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@movimiento_inventario.get("/movimiento-inventario/", response_model=List[schemas.schema_movimiento_inventario.MovimientoInventario], tags=["Movimientos Inventario"])
async def read_movimientos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    db_movimiento = crud.crud_movimiento_inventario.get_movimiento(db=db, skip=skip, limit=limit)
    return db_movimiento

@movimiento_inventario.get("/movimiento-inventario/{id}", response_model=schemas.schema_movimiento_inventario.MovimientoInventario, tags=["Movimientos Inventario"])
async def read_movimiento(id: int, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    db_movimiento = crud.crud_movimiento_inventario.get_movimiento_by_id(db=db, movimiento_id=id)
    if db_movimiento is None:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    return db_movimiento

@movimiento_inventario.get("/movimiento-inventario/producto/{producto_id}", response_model=List[schemas.schema_movimiento_inventario.MovimientoInventario], tags=["Movimientos Inventario"])
async def read_movimientos_by_producto(producto_id: int, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    db_movimiento = crud.crud_movimiento_inventario.get_movimientos_by_producto(db=db, producto_id=producto_id)
    return db_movimiento

@movimiento_inventario.post("/movimiento-inventario/", response_model=schemas.schema_movimiento_inventario.MovimientoInventario, tags=["Movimientos Inventario"])
def create_movimiento(movimiento: schemas.schema_movimiento_inventario.MovimientoInventarioCreate, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    return crud.crud_movimiento_inventario.create_movimiento(db=db, movimiento=movimiento)

@movimiento_inventario.delete("/movimiento-inventario/{id}", response_model=schemas.schema_movimiento_inventario.MovimientoInventario, tags=["Movimientos Inventario"])
async def delete_movimiento(id: int, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    db_movimiento = crud.crud_movimiento_inventario.delete_movimiento(db=db, id=id)
    if db_movimiento is None:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    return db_movimiento
