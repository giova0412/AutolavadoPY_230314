from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import config.db
import models.model_usuario
import models.model_auto
import models.model_services
import models.model_auto_servicio
import schemas.schema_reporte
from typing import List
import auth

reporte = APIRouter()

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@reporte.get("/reporte/{servicio_vehiculo_id}", response_model=schemas.schema_reporte.ReporteResponse, tags=["Reportes"])
async def get_reporte(
    servicio_vehiculo_id: int, 
    descuento: float = 0,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    vs = db.query(models.model_auto_servicio.VehiculoServicio).filter(
        models.model_auto_servicio.VehiculoServicio.Id == servicio_vehiculo_id
    ).first()
    
    if not vs:
        raise HTTPException(status_code=404, detail="Servicio de vehículo no encontrado")
    
    vehiculo = db.query(models.model_auto.Vehiculo).filter(
        models.model_auto.Vehiculo.Id == vs.vehiculo_Id
    ).first()
    
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    
    cliente = db.query(models.model_usuario.Usuario).filter(
        models.model_usuario.Usuario.Id == vehiculo.usuario_Id
    ).first()
    
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    servicio = db.query(models.model_services.Servicios).filter(
        models.model_services.Servicios.Id == vs.servicio_Id
    ).first()
    
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    
    cajero = db.query(models.model_usuario.Usuario).filter(
        models.model_usuario.Usuario.Id == vs.cajero_Id
    ).first()
    
    operativo = db.query(models.model_usuario.Usuario).filter(
        models.model_usuario.Usuario.Id == vs.operativo_Id
    ).first()
    
    if not cajero or not operativo:
        raise HTTPException(status_code=404, detail="Cajero u operativo no encontrado")
    
    total = servicio.costo - descuento
    if total < 0:
        total = 0
    
    reporte_data = {
        "id_servicio_vehiculo": vs.Id,
        "cliente_vehiculo": {
            "cliente_id": cliente.Id,
            "cliente_nombre": f"{cliente.nombre} {cliente.primer_apellido}",
            "vehiculo_id": vehiculo.Id,
            "vehiculo_placa": vehiculo.placa,
            "vehiculo_marca": vehiculo.marca,
            "vehiculo_modelo": vehiculo.modelo,
            "vehiculo_color": vehiculo.color
        },
        "servicio": {
            "servicio_id": servicio.Id,
            "servicio_nombre": servicio.nombre,
            "servicio_costo": servicio.costo
        },
        "operativo": {
            "usuario_id": operativo.Id,
            "usuario_nombre": f"{operativo.nombre} {operativo.primer_apellido}"
        },
        "cajero": {
            "usuario_id": cajero.Id,
            "usuario_nombre": f"{cajero.nombre} {cajero.primer_apellido}"
        },
        "descuento": descuento,
        "total": total,
        "fecha_servicio": vs.fecha,
        "hora_servicio": str(vs.hora)
    }
    
    return schemas.schema_reporte.ReporteResponse(
        success=True,
        data=reporte_data,
        message="Reporte generado exitosamente"
    )

@reporte.get("/reporte/", response_model=List[schemas.schema_reporte.ReporteResponse], tags=["Reportes"])
async def get_all_reportes(
    skip: int = 0, 
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    servicios_vehiculos = db.query(models.model_auto_servicio.VehiculoServicio).offset(skip).limit(limit).all()
    
    reportes = []
    
    for vs in servicios_vehiculos:
        vehiculo = db.query(models.model_auto.Vehiculo).filter(
            models.model_auto.Vehiculo.Id == vs.vehiculo_Id
        ).first()
        
        if not vehiculo:
            continue
            
        cliente = db.query(models.model_usuario.Usuario).filter(
            models.model_usuario.Usuario.Id == vehiculo.usuario_Id
        ).first()
        
        servicio = db.query(models.model_services.Servicios).filter(
            models.model_services.Servicios.Id == vs.servicio_Id
        ).first()
        
        cajero = db.query(models.model_usuario.Usuario).filter(
            models.model_usuario.Usuario.Id == vs.cajero_Id
        ).first()
        
        operativo = db.query(models.model_usuario.Usuario).filter(
            models.model_usuario.Usuario.Id == vs.operativo_Id
        ).first()
        
        if not all([cliente, servicio, cajero, operativo]):
            continue
        
        reporte_data = {
            "id_servicio_vehiculo": vs.Id,
            "cliente_vehiculo": {
                "cliente_id": cliente.Id,
                "cliente_nombre": f"{cliente.nombre} {cliente.primer_apellido}",
                "vehiculo_id": vehiculo.Id,
                "vehiculo_placa": vehiculo.placa,
                "vehiculo_marca": vehiculo.marca,
                "vehiculo_modelo": vehiculo.modelo,
                "vehiculo_color": vehiculo.color
            },
            "servicio": {
                "servicio_id": servicio.Id,
                "servicio_nombre": servicio.nombre,
                "servicio_costo": servicio.costo
            },
            "operativo": {
                "usuario_id": operativo.Id,
                "usuario_nombre": f"{operativo.nombre} {operativo.primer_apellido}"
            },
            "cajero": {
                "usuario_id": cajero.Id,
                "usuario_nombre": f"{cajero.nombre} {cajero.primer_apellido}"
            },
            "descuento": 0,
            "total": servicio.costo,
            "fecha_servicio": vs.fecha,
            "hora_servicio": str(vs.hora)
        }
        
        reportes.append(schemas.schema_reporte.ReporteResponse(
            success=True,
            data=reporte_data,
            message=None
        ))
    
    return reportes
