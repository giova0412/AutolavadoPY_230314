'''CRUD completo para el modelo Auto'''
from sqlalchemy.orm import Session
from datetime import datetime
import models.auto as model_auto
import schemas.schema_auto as schema_auto

def get_autos(db: Session, skip: int = 0, limit: int = 100):
    '''Obtener listado de autos'''
    return db.query(model_auto.Auto).offset(skip).limit(limit).all()

def get_auto(db: Session, auto_id: int):
    '''Obtener un auto por su ID'''
    return db.query(model_auto.Auto).filter(model_auto.Auto.id == auto_id).first()

def get_auto_by_placa(db: Session, placa: str):
    '''Obtener un auto por su placa'''
    return db.query(model_auto.Auto).filter(model_auto.Auto.placa == placa).first()

def create_auto(db: Session, auto: schema_auto.AutoCreate):
    '''Crear un nuevo auto'''
    db_auto = model_auto.Auto(
        usuario_id=auto.usuario_id,
        modelo=auto.modelo,
        placa=auto.placa,
        serie=auto.serie,
        color=auto.color,
        tipo=auto.tipo,
        anio=auto.anio,
        estado=auto.estado,
        marca=auto.marca,
        fecha_registro=datetime.now(),
        fecha_actualizacion=datetime.now()
    )
    db.add(db_auto)
    db.commit()
    db.refresh(db_auto)
    return db_auto

def update_auto(db: Session, auto_id: int, auto: schema_auto.AutoUpdate):
    '''Actualizar un auto existente'''
    db_auto = db.query(model_auto.Auto).filter(model_auto.Auto.id == auto_id).first()
    if db_auto is None:
        return None
    update_data = auto.dict(exclude_unset=True)
    update_data["fecha_actualizacion"] = datetime.now()
    for key, value in update_data.items():
        setattr(db_auto, key, value)
    db.commit()
    db.refresh(db_auto)
    return db_auto

def delete_auto(db: Session, auto_id: int):
    '''Eliminar un auto (borrado lógico)'''
    db_auto = db.query(model_auto.Auto).filter(model_auto.Auto.id == auto_id).first()
    if db_auto is None:
        return None
    db_auto.estado = False
    db_auto.fecha_actualizacion = datetime.now()
    db.commit()
    db.refresh(db_auto)
    return db_auto