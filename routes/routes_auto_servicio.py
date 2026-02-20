'''Rutas CRUD para el modelo AutoServicio (relación auto-servicio)'''
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import crud.crud_auto_servicio as crud_auto_servicio
import schemas.schema_auto_servicio as schema_auto_servicio
from config.db import SessionLocal

router = APIRouter(
    prefix="/auto-servicios",
    tags=["Auto-Servicios"],
    responses={404: {"description": "No encontrado"}}
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schema_auto_servicio.Auto_Servicio], summary="Listar todos los registros de auto-servicio")
def listar_auto_servicios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    '''Retorna el listado completo de registros de servicios asignados a autos.'''
    return crud_auto_servicio.get_auto_servicios(db, skip=skip, limit=limit)

@router.get("/{auto_servicio_id}", response_model=schema_auto_servicio.Auto_Servicio, summary="Obtener un registro auto-servicio por ID")
def obtener_auto_servicio(auto_servicio_id: int, db: Session = Depends(get_db)):
    '''Retorna los datos de un registro auto-servicio específico por su ID.'''
    db_as = crud_auto_servicio.get_auto_servicio(db, auto_servicio_id=auto_servicio_id)
    if db_as is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro no encontrado")
    return db_as

@router.post("/", response_model=schema_auto_servicio.Auto_Servicio, status_code=status.HTTP_201_CREATED, summary="Registrar un auto para un servicio")
def crear_auto_servicio(auto_servicio: schema_auto_servicio.Auto_ServicioCreate, db: Session = Depends(get_db)):
    '''Crea un nuevo registro que asigna un servicio a un auto (programación de lavado).'''
    return crud_auto_servicio.create_auto_servicio(db=db, auto_servicio=auto_servicio)

@router.put("/{auto_servicio_id}", response_model=schema_auto_servicio.Auto_Servicio, summary="Actualizar un registro auto-servicio")
def actualizar_auto_servicio(auto_servicio_id: int, auto_servicio: schema_auto_servicio.Auto_ServicioUpdate, db: Session = Depends(get_db)):
    '''Actualiza los datos de un registro auto-servicio (ej: cambiar estatus a "En Proceso" o "Realizado").'''
    db_as = crud_auto_servicio.update_auto_servicio(db=db, auto_servicio_id=auto_servicio_id, auto_servicio=auto_servicio)
    if db_as is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro no encontrado")
    return db_as

@router.delete("/{auto_servicio_id}", response_model=schema_auto_servicio.Auto_Servicio, summary="Eliminar un registro auto-servicio (lógico)")
def eliminar_auto_servicio(auto_servicio_id: int, db: Session = Depends(get_db)):
    '''Desactiva un registro auto-servicio (borrado lógico: estado=False).'''
    db_as = crud_auto_servicio.delete_auto_servicio(db=db, auto_servicio_id=auto_servicio_id)
    if db_as is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro no encontrado")
    return db_as
