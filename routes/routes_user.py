'''Rutas CRUD para el modelo User (Usuarios)'''
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import crud.crud_user as crud_user
import schemas.schema_user as schema_user
from config.db import SessionLocal

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
    responses={404: {"description": "No encontrado"}}
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schema_user.User], summary="Listar todos los usuarios")
def listar_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    '''Retorna el listado completo de usuarios registrados.'''
    return crud_user.get_users(db, skip=skip, limit=limit)

@router.get("/{usuario_id}", response_model=schema_user.User, summary="Obtener usuario por ID")
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    '''Retorna los datos de un usuario específico por su ID.'''
    db_user = crud_user.get_user(db, user_id=usuario_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return db_user

@router.post("/", response_model=schema_user.User, status_code=status.HTTP_201_CREATED, summary="Crear un nuevo usuario")
def crear_usuario(usuario: schema_user.UserCreate, db: Session = Depends(get_db)):
    '''Crea un nuevo usuario en el sistema.'''
    db_user = crud_user.get_user_by_email(db, correo=usuario.correo_electronico)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El correo electrónico ya está registrado")
    return crud_user.create_user(db=db, user=usuario)

@router.put("/{usuario_id}", response_model=schema_user.User, summary="Actualizar un usuario")
def actualizar_usuario(usuario_id: int, usuario: schema_user.UserUpdate, db: Session = Depends(get_db)):
    '''Actualiza los datos de un usuario existente.'''
    db_user = crud_user.update_user(db=db, user_id=usuario_id, user=usuario)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return db_user

@router.delete("/{usuario_id}", response_model=schema_user.User, summary="Eliminar un usuario (lógico)")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    '''Desactiva un usuario (borrado lógico: estatus=False).'''
    db_user = crud_user.delete_user(db=db, user_id=usuario_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return db_user
