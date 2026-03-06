from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import config.db
import crud.crud_producto
import schemas.schema_producto
import models.model_producto
from typing import List
import auth

producto = APIRouter()

models.model_producto.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@producto.get("/producto/", response_model=List[schemas.schema_producto.Producto], tags=["Productos"])
async def read_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    db_producto = crud.crud_producto.get_producto(db=db, skip=skip, limit=limit)
    return db_producto

@producto.get("/producto/{id}", response_model=schemas.schema_producto.Producto, tags=["Productos"])
async def read_producto(id: int, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    db_producto = crud.crud_producto.get_producto_by_id(db=db, producto_id=id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@producto.post("/producto/", response_model=schemas.schema_producto.Producto, tags=["Productos"])
def create_producto(producto: schemas.schema_producto.ProductoCreate, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    db_producto = crud.crud_producto.get_producto_by_nombre(db, nombre=producto.nombre)
    if db_producto:
        raise HTTPException(status_code=400, detail="Producto existente")
    return crud.crud_producto.create_producto(db=db, producto=producto)

@producto.put("/producto/{id}", response_model=schemas.schema_producto.Producto, tags=["Productos"])
async def update_producto(id: int, producto: schemas.schema_producto.ProductoUpdate, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    db_producto = crud.crud_producto.update_producto(db=db, id=id, producto=producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@producto.delete("/producto/{id}", response_model=schemas.schema_producto.Producto, tags=["Productos"])
async def delete_producto(id: int, db: Session = Depends(get_db), current_user: str = Depends(auth.get_current_user)):
    db_producto = crud.crud_producto.delete_producto(db=db, id=id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto
