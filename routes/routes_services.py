'''Rutas CRUD para el modelo Service (Servicios)'''
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import crud.crud_services as crud_services
import schemas.schema_services as schema_services
from config.db import SessionLocal

router = APIRouter(
    prefix="/servicios",
    tags=["Servicios"],
    responses={404: {"description": "No encontrado"}}
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schema_services.Servicio], summary="Listar todos los servicios")
def listar_servicios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    '''Retorna el listado completo de servicios disponibles.'''
    return crud_services.get_servicios(db, skip=skip, limit=limit)

@router.get("/{servicio_id}", response_model=schema_services.Servicio, summary="Obtener un servicio por ID")
def obtener_servicio(servicio_id: int, db: Session = Depends(get_db)):
    '''Retorna los datos de un servicio específico por su ID.'''
    db_servicio = crud_services.get_servicio(db, servicio_id=servicio_id)
    if db_servicio is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Servicio no encontrado")
    return db_servicio

@router.post("/", response_model=schema_services.Servicio, status_code=status.HTTP_201_CREATED, summary="Crear un nuevo servicio")
def crear_servicio(servicio: schema_services.ServicioCreate, db: Session = Depends(get_db)):
    '''Crea un nuevo servicio en el catálogo del autolavado.'''
    return crud_services.create_servicio(db=db, servicio=servicio)

@router.put("/{servicio_id}", response_model=schema_services.Servicio, summary="Actualizar un servicio")
def actualizar_servicio(servicio_id: int, servicio: schema_services.ServicioUpdate, db: Session = Depends(get_db)):
    '''Actualiza los datos de un servicio existente.'''
    db_servicio = crud_services.update_servicio(db=db, servicio_id=servicio_id, servicio=servicio)
    if db_servicio is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Servicio no encontrado")
    return db_servicio

@router.delete("/{servicio_id}", response_model=schema_services.Servicio, summary="Eliminar un servicio (lógico)")
def eliminar_servicio(servicio_id: int, db: Session = Depends(get_db)):
    '''Desactiva un servicio (borrado lógico: estado=False).'''
    db_servicio = crud_services.delete_servicio(db=db, servicio_id=servicio_id)
    if db_servicio is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Servicio no encontrado")
    return db_servicio
