'''CRUD completo para el modelo AutoServicio'''
from sqlalchemy.orm import Session
from datetime import datetime
import models.auto_servicio as model_auto_servicio
import schemas.schema_auto_servicio as schema_auto_servicio

def get_auto_servicios(db: Session, skip: int = 0, limit: int = 100):
    '''Obtener listado de registros auto-servicio'''
    return db.query(model_auto_servicio.AutoServicio).offset(skip).limit(limit).all()

def get_auto_servicio(db: Session, auto_servicio_id: int):
    '''Obtener un registro auto-servicio por su ID'''
    return db.query(model_auto_servicio.AutoServicio).filter(
        model_auto_servicio.AutoServicio.id == auto_servicio_id
    ).first()

def create_auto_servicio(db: Session, auto_servicio: schema_auto_servicio.Auto_ServicioCreate):
    '''Crear un nuevo registro auto-servicio'''
    db_auto_servicio = model_auto_servicio.AutoServicio(
        auto_id=auto_servicio.auto_id,
        cajero_id=auto_servicio.cajero_id,
        operador_id=auto_servicio.operador_id,
        servicio_id=auto_servicio.servicio_id,
        fecha=auto_servicio.fecha,
        estatus=auto_servicio.estatus,
        estado=auto_servicio.estado,
        fecha_registro=datetime.now(),
        fecha_actualizacion=datetime.now()
    )
    db.add(db_auto_servicio)
    db.commit()
    db.refresh(db_auto_servicio)
    return db_auto_servicio

def update_auto_servicio(db: Session, auto_servicio_id: int, auto_servicio: schema_auto_servicio.Auto_ServicioUpdate):
    '''Actualizar un registro auto-servicio existente'''
    db_as = db.query(model_auto_servicio.AutoServicio).filter(
        model_auto_servicio.AutoServicio.id == auto_servicio_id
    ).first()
    if db_as is None:
        return None
    update_data = auto_servicio.dict(exclude_unset=True)
    update_data["fecha_actualizacion"] = datetime.now()
    for key, value in update_data.items():
        setattr(db_as, key, value)
    db.commit()
    db.refresh(db_as)
    return db_as

def delete_auto_servicio(db: Session, auto_servicio_id: int):
    '''Eliminar un registro auto-servicio (borrado lógico)'''
    db_as = db.query(model_auto_servicio.AutoServicio).filter(
        model_auto_servicio.AutoServicio.id == auto_servicio_id
    ).first()
    if db_as is None:
        return None
    db_as.estado = False
    db_as.fecha_actualizacion = datetime.now()
    db.commit()
    db.refresh(db_as)
    return db_as
