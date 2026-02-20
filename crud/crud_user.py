'''CRUD completo para el modelo User'''
from sqlalchemy.orm import Session
from datetime import datetime
import models.User as model_user
import schemas.schema_user as schema_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    '''Obtener listado de usuarios'''
    return db.query(model_user.User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    '''Obtener un usuario por su ID'''
    return db.query(model_user.User).filter(model_user.User.id == user_id).first()

def get_user_by_email(db: Session, correo: str):
    '''Obtener un usuario por correo electrónico'''
    return db.query(model_user.User).filter(model_user.User.correo_electronico == correo).first()

def create_user(db: Session, user: schema_user.UserCreate):
    '''Crear un nuevo usuario'''
    db_user = model_user.User(
        rol_id=user.rol_id,
        nombre=user.nombre,
        primer_apellido=user.primer_apellido,
        segundo_apellido=user.segundo_apellido,
        direccion=user.direccion,
        correo_electronico=user.correo_electronico,
        numero_telefono=user.numero_telefono,
        contrasena=user.contrasena,
        estatus=user.estatus,
        fecha_registro=datetime.now(),
        fecha_actualizacion=datetime.now()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schema_user.UserUpdate):
    '''Actualizar un usuario existente'''
    db_user = db.query(model_user.User).filter(model_user.User.id == user_id).first()
    if db_user is None:
        return None
    update_data = user.dict(exclude_unset=True)
    update_data["fecha_actualizacion"] = datetime.now()
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    '''Eliminar un usuario (borrado lógico)'''
    db_user = db.query(model_user.User).filter(model_user.User.id == user_id).first()
    if db_user is None:
        return None
    db_user.estatus = False
    db_user.fecha_actualizacion = datetime.now()
    db.commit()
    db.refresh(db_user)
    return db_user