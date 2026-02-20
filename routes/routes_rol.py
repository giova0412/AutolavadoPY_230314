'''Rutas CRUD para el modelo Rol'''
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import crud.crud_rol as crud_rol
import schemas.schema_rol as schema_rol
from config.db import SessionLocal

router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
    responses={404: {"description": "No encontrado"}}
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schema_rol.Rol], summary="Listar todos los roles")
def listar_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    '''Retorna el listado completo de roles registrados en el sistema.'''
    roles = crud_rol.get_roles(db, skip=skip, limit=limit)
    return roles

@router.get("/{rol_id}", response_model=schema_rol.Rol, summary="Obtener un rol por ID")
def obtener_rol(rol_id: int, db: Session = Depends(get_db)):
    '''Retorna los datos de un rol específico por su ID.'''
    db_rol = crud_rol.get_rol(db, rol_id=rol_id)
    if db_rol is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    return db_rol

@router.post("/", response_model=schema_rol.Rol, status_code=status.HTTP_201_CREATED, summary="Crear un nuevo rol")
def crear_rol(rol: schema_rol.RolCreate, db: Session = Depends(get_db)):
    '''Crea un nuevo rol en el sistema.'''
    return crud_rol.create_rol(db=db, rol=rol)

@router.put("/{rol_id}", response_model=schema_rol.Rol, summary="Actualizar un rol")
def actualizar_rol(rol_id: int, rol: schema_rol.RolUpdate, db: Session = Depends(get_db)):
    '''Actualiza los datos de un rol existente.'''
    db_rol = crud_rol.update_rol(db=db, rol_id=rol_id, rol=rol)
    if db_rol is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    return db_rol

@router.delete("/{rol_id}", response_model=schema_rol.Rol, summary="Eliminar un rol (lógico)")
def eliminar_rol(rol_id: int, db: Session = Depends(get_db)):
    '''Desactiva un rol (borrado lógico: estado=False).'''
    db_rol = crud_rol.delete_rol(db=db, rol_id=rol_id)
    if db_rol is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    return db_rol