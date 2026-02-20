'''Rutas CRUD para el modelo Auto'''
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import crud.crud_auto as crud_auto
import schemas.schema_auto as schema_auto
from config.db import SessionLocal

router = APIRouter(
    prefix="/autos",
    tags=["Autos"],
    responses={404: {"description": "No encontrado"}}
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schema_auto.Auto], summary="Listar todos los autos")
def listar_autos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    '''Retorna el listado completo de autos registrados.'''
    return crud_auto.get_autos(db, skip=skip, limit=limit)

@router.get("/{auto_id}", response_model=schema_auto.Auto, summary="Obtener un auto por ID")
def obtener_auto(auto_id: int, db: Session = Depends(get_db)):
    '''Retorna los datos de un auto específico por su ID.'''
    db_auto = crud_auto.get_auto(db, auto_id=auto_id)
    if db_auto is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Auto no encontrado")
    return db_auto

@router.post("/", response_model=schema_auto.Auto, status_code=status.HTTP_201_CREATED, summary="Registrar un nuevo auto")
def crear_auto(auto: schema_auto.AutoCreate, db: Session = Depends(get_db)):
    '''Registra un nuevo auto en el sistema. La placa debe ser única.'''
    db_auto = crud_auto.get_auto_by_placa(db, placa=auto.placa)
    if db_auto:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ya existe un auto con esa placa")
    return crud_auto.create_auto(db=db, auto=auto)

@router.put("/{auto_id}", response_model=schema_auto.Auto, summary="Actualizar un auto")
def actualizar_auto(auto_id: int, auto: schema_auto.AutoUpdate, db: Session = Depends(get_db)):
    '''Actualiza los datos de un auto existente.'''
    db_auto = crud_auto.update_auto(db=db, auto_id=auto_id, auto=auto)
    if db_auto is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Auto no encontrado")
    return db_auto

@router.delete("/{auto_id}", response_model=schema_auto.Auto, summary="Eliminar un auto (lógico)")
def eliminar_auto(auto_id: int, db: Session = Depends(get_db)):
    '''Desactiva un auto (borrado lógico: estado=False).'''
    db_auto = crud_auto.delete_auto(db=db, auto_id=auto_id)
    if db_auto is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Auto no encontrado")
    return db_auto
