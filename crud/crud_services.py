'''CRUD completo para el modelo Service (Servicios)'''
from sqlalchemy.orm import Session
from datetime import datetime
import models.services as model_services
import schemas.schema_services as schema_services

def get_servicios(db: Session, skip: int = 0, limit: int = 100):
    '''Obtener listado de servicios'''
    return db.query(model_services.Service).offset(skip).limit(limit).all()

def get_servicio(db: Session, servicio_id: int):
    '''Obtener un servicio por su ID'''
    return db.query(model_services.Service).filter(model_services.Service.id == servicio_id).first()

def create_servicio(db: Session, servicio: schema_services.ServicioCreate):
    '''Crear un nuevo servicio'''
    db_servicio = model_services.Service(
        nombre=servicio.nombre,
        descripcion=servicio.descripcion,
        costo=servicio.costo,
        duracion=servicio.duracion,
        estado=servicio.estado,
        fecha_registro=datetime.now(),
        fecha_actualizacion=datetime.now()
    )
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

def update_servicio(db: Session, servicio_id: int, servicio: schema_services.ServicioUpdate):
    '''Actualizar un servicio existente'''
    db_servicio = db.query(model_services.Service).filter(model_services.Service.id == servicio_id).first()
    if db_servicio is None:
        return None
    update_data = servicio.dict(exclude_unset=True)
    update_data["fecha_actualizacion"] = datetime.now()
    for key, value in update_data.items():
        setattr(db_servicio, key, value)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

def delete_servicio(db: Session, servicio_id: int):
    '''Eliminar un servicio (borrado lógico)'''
    db_servicio = db.query(model_services.Service).filter(model_services.Service.id == servicio_id).first()
    if db_servicio is None:
        return None
    db_servicio.estado = False
    db_servicio.fecha_actualizacion = datetime.now()
    db.commit()
    db.refresh(db_servicio)
    return db_servicio