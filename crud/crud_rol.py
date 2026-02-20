'''CRUD completo para el modelo Rol'''
from sqlalchemy.orm import Session
from datetime import datetime
import models.rol as model_rol
import schemas.schema_rol as schema_rol

def get_roles(db: Session, skip: int = 0, limit: int = 100):
    '''Obtener listado de roles'''
    return db.query(model_rol.Rol).offset(skip).limit(limit).all()

def get_rol(db: Session, rol_id: int):
    '''Obtener un rol por su ID'''
    return db.query(model_rol.Rol).filter(model_rol.Rol.id == rol_id).first()

def create_rol(db: Session, rol: schema_rol.RolCreate):
    '''Crear un nuevo rol'''
    db_rol = model_rol.Rol(
        nombre_rol=rol.nombre_rol,
        estado=rol.estado,
        fecha_registro=datetime.now(),
        fecha_modificacion=datetime.now()
    )
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

def update_rol(db: Session, rol_id: int, rol: schema_rol.RolUpdate):
    '''Actualizar un rol existente'''
    db_rol = db.query(model_rol.Rol).filter(model_rol.Rol.id == rol_id).first()
    if db_rol is None:
        return None
    update_data = rol.dict(exclude_unset=True)
    update_data["fecha_modificacion"] = datetime.now()
    for key, value in update_data.items():
        setattr(db_rol, key, value)
    db.commit()
    db.refresh(db_rol)
    return db_rol

def delete_rol(db: Session, rol_id: int):
    '''Eliminar un rol (borrado lógico)'''
    db_rol = db.query(model_rol.Rol).filter(model_rol.Rol.id == rol_id).first()
    if db_rol is None:
        return None
    db_rol.estado = False
    db_rol.fecha_modificacion = datetime.now()
    db.commit()
    db.refresh(db_rol)
    return db_rol