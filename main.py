'''
Punto de entrada principal de la API del Sistema de Autolavado
Documentación Swagger disponible en: http://localhost:8000/docs
Documentación ReDoc disponible en:  http://localhost:8000/redoc
'''
from fastapi import FastAPI
from config.db import Base, engine

# Importar modelos para crear tablas
import models.rol
import models.User
import models.services
import models.auto
import models.auto_servicio

# Importar routers
from routes.routes_rol import router as router_rol
from routes.routes_user import router as router_user
from routes.routes_auto import router as router_auto
from routes.routes_services import router as router_services
from routes.routes_auto_servicio import router as router_auto_servicio

# Crear todas las tablas en la base de datos (si no existen)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Autolavado API",
    description="""
## API REST para el Sistema de Autolavado

Gestiona todos los recursos del sistema:

- **Roles** – Administra los roles de usuario (admin, cajero, operador, etc.)
- **Usuarios** – Gestión de usuarios del sistema
- **Autos** – Registro de vehículos de clientes
- **Servicios** – Catálogo de servicios de lavado disponibles
- **Auto-Servicios** – Programación y seguimiento de servicios a autos
    """,
    version="1.0.0",
    contact={
        "name": "Sistema de Autolavado",
    },
    license_info={
        "name": "MIT",
    },
)

# Registrar todos los routers
app.include_router(router_rol)
app.include_router(router_user)
app.include_router(router_auto)
app.include_router(router_services)
app.include_router(router_auto_servicio)

@app.get("/", tags=["Root"], summary="Bienvenida a la API")
def root():
    '''Endpoint de bienvenida. Visita /docs para la documentación Swagger.'''
    return {
        "mensaje": "Bienvenido al Sistema de Autolavado API",
        "documentacion": "/docs",
        "redoc": "/redoc"
    }