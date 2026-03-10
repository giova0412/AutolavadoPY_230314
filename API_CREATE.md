# Documentación de Endpoints - Autolavado API

## Headers requeridos para todos los endpoints (excepto login)

```http
Authorization: Bearer <token>
Content-Type: application/json
```

---

## FLUJO COMPLETO PARA REGISTRAR UN SERVICIO

Antes de usar **auto-servicio**, necesitas crear estos datos en orden:

```
1. ROLES       → (ya existen) Crear si necesitas más
2. USUARIOS    → Crear: cliente, cajero, operativo
3. SERVICIOS   → Crear los tipos de servicio
4. VEHÍCULOS   → Registrar vehículo del cliente
5. AUTO-SERVICIO → Registrar el servicio
6. REPORTE     → Generar reporte con descuento
```

---

## 0. ROLES (ya existen)

### GET /rol/

Lista los roles disponibles. Typical:

| ID | Rol | Descripción |
|----|-----|-------------|
| 1 | admin | Administrador del sistema |
| 2 | cajero | Encargado de cobros |
| 3 | operativo | Persona que realiza el servicio |
| 4 | cliente | Dueño del vehículo |

### ⚠️ ROLES NECESARIOS PARA AUTO-SERVICIO

Para crear un **auto-servicio** necesitas crear usuarios con estos roles:

| Campo en auto-servicio | Rol requerido | Ejemplo |
|----------------------|---------------|---------|
| `cajero_Id` | cajero (ID 2) | Usuario que cobra |
| `operativo_Id` | operativo (ID 3) | Usuario que lava el auto |
| `usuario_Id` (en vehículo) | cliente (ID 4) | Dueño del vehículo |

---

## 1. USUARIOS

### POST /usuario/

**Crea un nuevo usuario (cliente, cajero, operativo)**

```json
{
  "rol_Id": 4,
  "nombre": "Juan",
  "primer_apellido": "Perez",
  "segundo_apellido": "Gomez",
  "direccion": "Calle Principal 123",
  "correo_electronico": "juan@example.com",
  "numero_telefono": "1234567890",
  "contrasena": "password123",
  "estado": true,
  "fecha_registro": "2026-03-06T10:00:00",
  "fecha_actualizacion": "2026-03-06T10:00:00"
}
```

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| rol_Id | int | Sí | ID del rol (1=admin, 2=cajero, 3=operativo, 4=cliente) |
| nombre | string | Sí | Nombre del usuario |
| primer_apellido | string | Sí | Primer apellido |
| segundo_apellido | string | Sí | Segundo apellido |
| direccion | string | Sí | Dirección |
| correo_electronico | string | Sí | Correo electrónico (único) |
| numero_telefono | string | Sí | Teléfono (único) |
| contrasena | string | Sí | Contraseña |
| estado | boolean | Sí | true = activo |
| fecha_registro | datetime | Sí | Fecha de registro |
| fecha_actualizacion | datetime | Sí | Fecha de actualización |

---

## 2. SERVICIOS

### POST /services/

**Crea un tipo de servicio (lavado, encerado, etc.)**

```json
{
  "nombre": "Lavado Premium",
  "descripcion": "Lavado completo con shampoo y encerado",
  "costo": 200.00,
  "duracion_minutos": 45,
  "estado": true,
  "fecha_registro": "2026-03-06T10:00:00",
  "fecha_actualizacion": "2026-03-06T10:00:00"
}
```

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| nombre | string | Sí | Nombre del servicio |
| descripcion | string | Sí | Descripción |
| costo | float | Sí | Precio del servicio |
| duracion_minutos | int | Sí | Duración en minutos |
| estado | boolean | Sí | true = activo |
| fecha_registro | datetime | Sí | Fecha de registro |
| fecha_actualizacion | datetime | Sí | Fecha de actualización |

---

## 3. VEHÍCULOS

### POST /autos/

**Registra un nuevo vehículo**

```json
{
  "usuario_Id": 1,
  "placa": "ABC-1234",
  "marca": "Toyota",
  "modelo": "Corolla",
  "serie": "1HGBH41JXMN109186",
  "color": "Blanco",
  "tipo": "Sedán",
  "anio": "2023",
  "estado": true,
  "fecha_registro": "2026-03-06T10:00:00",
  "fecha_actualizacion": "2026-03-06T10:00:00"
}
```

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| usuario_Id | int | Sí | ID del cliente (dueño) - debe existir |
| placa | string | Sí | Placa única del vehículo |
| marca | string | Sí | Marca del auto |
| modelo | string | Sí | Modelo del auto |
| serie | string | No | Número de serie (VIN) |
| color | string | Sí | Color del vehículo |
| tipo | string | Sí | Tipo (Sedán, SUV, Pickup, etc.) |
| anio | string | Sí | Año del vehículo |
| estado | boolean | Sí | true = activo |
| fecha_registro | datetime | Sí | Fecha de registro |
| fecha_actualizacion | datetime | Sí | Fecha de actualización |

---

## 4. PRODUCTOS

### POST /producto/

**Crea un nuevo producto en el inventario**

```json
{
  "nombre": "Shampoo Premium",
  "descripcion": "Shampoo para auto de grado automotriz",
  "categoria": "Limpieza",
  "unidad_medida": "litro",
  "stock_actual": 50,
  "stock_minimo": 10,
  "precio": 150.00,
  "fecha_registro": "2026-03-06T10:00:00",
  "fecha_actualizacion": "2026-03-06T10:00:00",
  "estado": true
}
```

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| nombre | string | Sí | Nombre del producto |
| descripcion | string | Sí | Descripción detallada |
| categoria | string | Sí | Categoría (Limpieza, Químicos, etc.) |
| unidad_medida | string | Sí | Unidad (litro, kilo, pieza) |
| stock_actual | float | Sí | Cantidad actual en inventario |
| stock_minimo | float | Sí | Stock mínimo para alertas |
| precio | float | Sí | Precio unitario |
| fecha_registro | datetime | Sí | Fecha de registro (ISO 8601) |
| fecha_actualizacion | datetime | Sí | Fecha de actualización |
| estado | boolean | Sí | true = activo, false = inactivo |

---

## 2. MOVIMIENTOS INVENTARIO

### POST /movimiento-inventario/

**Registra entrada o salida de productos**

```json
{
  "producto_Id": 1,
  "tipo_movimiento": "entrada",
  "cantidad": 20,
  "fecha_movimiento": "2026-03-06T10:00:00",
  "usuario_Id": 1
}
```

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| producto_Id | int | Sí | ID del producto (debe existir) |
| tipo_movimiento | string | Sí | "entrada" o "salida" |
| cantidad | int | Sí | Cantidad a ingresar o retirar |
| fecha_movimiento | datetime | Sí | Fecha del movimiento |
| usuario_Id | int | Sí | ID del usuario que registra |

---

## 3. VEHÍCULOS

### POST /autos/

**Registra un nuevo vehículo**

```json
{
  "usuario_Id": 1,
  "placa": "ABC-1234",
  "marca": "Toyota",
  "modelo": "Corolla",
  "serie": "1HGBH41JXMN109186",
  "color": "Blanco",
  "tipo": "Sedán",
  "anio": "2023",
  "estado": true,
  "fecha_registro": "2026-03-06T10:00:00",
  "fecha_actualizacion": "2026-03-06T10:00:00"
}
```

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| usuario_Id | int | Sí | ID del cliente (dueño) |
| placa | string | Sí | Placa única del vehículo |
| marca | string | Sí | Marca del auto |
| modelo | string | Sí | Modelo del auto |
| serie | string | No | Número de serie (VIN) |
| color | string | Sí | Color del vehículo |
| tipo | string | Sí | Tipo (Sedán, SUV, Pickup, etc.) |
| anio | string | Sí | Año del vehículo |
| estado | boolean | Sí | true = activo |
| fecha_registro | Fecha de registro |
 datetime | Sí || fecha_actualizacion | datetime | Sí | Fecha de actualización |

---

## 5. AUTO SERVICIO

> ⚠️ **REQUISITOS PREVIOS:** Antes de crear un auto-servicio, necesitas:
> - 1 usuario con rol **cliente** (ID 4) → Dueño del vehículo
> - 1 usuario con rol **cajero** (ID 2) → Quien cobra
> - 1 usuario con rol **operativo** (ID 3) → Quien hace el servicio
> - 1 vehículo registrado
> - 1 servicio creado

### POST /auto-servicio/

**Registra un servicio realizado a un vehículo**

```json
{
  "vehiculo_Id": 1,
  "cajero_Id": 1,
  "operativo_Id": 2,
  "servicio_Id": 1,
  "fecha": "2026-03-06",
  "hora": "10:30:00",
  "estatus": "completado",
  "estado": true,
  "fecha_registro": "2026-03-06T10:00:00",
  "fecha_actualizacion": "2026-03-06T10:00:00"
}
```

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| vehiculo_Id | int | Sí | ID del vehículo (debe existir) |
| cajero_Id | int | Sí | ID del usuario cajero |
| operativo_Id | int | Sí | ID del usuario que realizó el servicio |
| servicio_Id | int | Sí | ID del servicio (debe existir en tbc_servicios) |
| fecha | date | Sí | Fecha del servicio (YYYY-MM-DD) |
| hora | time | Sí | Hora del servicio (HH:MM:SS) |
| estatus | string | Sí | Estado: "pendiente", "en_proceso", "completado", "cancelado" |
| estado | boolean | Sí | true = activo |
| fecha_registro | datetime | Sí | Fecha de registro |
| fecha_actualizacion | datetime | Sí | Fecha de actualización |

---

## 6. REPORTE

### POST /auto-servicio/

**Registra un servicio realizado a un vehículo**

```json
{
  "vehiculo_Id": 1,
  "cajero_Id": 1,
  "operativo_Id": 2,
  "servicio_Id": 1,
  "fecha": "2026-03-06",
  "hora": "10:30:00",
  "estatus": "completado",
  "estado": true,
  "fecha_registro": "2026-03-06T10:00:00",
  "fecha_actualizacion": "2026-03-06T11:00:00"
}
```

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| vehiculo_Id | int | Sí | ID del vehículo |
| cajero_Id | int | Sí | ID del usuario cajero |
| operativo_Id | int | Sí | ID del usuario que realizó el servicio |
| servicio_Id | int | Sí | ID del servicio (de tbc_servicios) |
| fecha | date | Sí | Fecha del servicio (YYYY-MM-DD) |
| hora | time | Sí | Hora del servicio (HH:MM:SS) |
| estatus | string | Sí | Estado: "pendiente", "en_proceso", "completado", "cancelado" |
| estado | boolean | Sí | true = activo |
| fecha_registro | datetime | Sí | Fecha de registro |
| fecha_actualizacion | datetime | Sí | Fecha de actualización |

---

## 6. REPORTE

### GET /reporte/{servicio_vehiculo_id}?descuento=0

**Genera reporte con datos del servicio, cliente, vehículo, descuentos y total**

**Parámetros:**
- `servicio_vehiculo_id` (path) - ID del registro en auto-servicio
- `descuento` (query) - Descuento a aplicar (default: 0)

**Ejemplo:**
```
GET /reporte/1?descuento=50
```

**Respuesta:**

```json
{
  "success": true,
  "data": {
    "id_servicio_vehiculo": 1,
    "cliente_vehiculo": {
      "cliente_id": 1,
      "cliente_nombre": "Juan Perez",
      "vehiculo_id": 1,
      "vehiculo_placa": "ABC-1234",
      "vehiculo_marca": "Toyota",
      "vehiculo_modelo": "Corolla",
      "vehiculo_color": "Blanco"
    },
    "servicio": {
      "servicio_id": 1,
      "servicio_nombre": "Lavado Premium",
      "servicio_costo": 200.00
    },
    "operativo": {
      "usuario_id": 2,
      "usuario_nombre": "Carlos Lopez"
    },
    "cajero": {
      "usuario_id": 1,
      "usuario_nombre": "Maria Garcia"
    },
    "descuento": 50.00,
    "total": 150.00,
    "fecha_servicio": "2026-03-06",
    "hora_servicio": "10:30:00"
  },
  "message": "Reporte generado exitosamente"
}
```

---

## Cómo obtener el token (login)

### POST /login/

```http
Content-Type: application/x-www-form-urlencoded

username=tu_correo_o_telefono&password=tu_contraseña
```

**Respuesta:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

Usa este token en el header `Authorization: Bearer <token>` para los demás endpoints.

---

## Notas importantes

1. Los campos de fecha deben estar en formato ISO 8601: `YYYY-MM-DDTHH:MM:SS`
2. Para fechas simples (fecha, hora) usa los formatos indicados en cada tabla
3. Todos los IDs (producto_Id, usuario_Id, etc.) deben existir previamente en la base de datos
4. El campo `placa` en vehículos es único - no puedes registrar dos autos con la misma placa

---

## EJEMPLO COMPLETO: Registro de un servicio

### Paso 1: Crear usuario cliente
```json
POST /usuario/
{
  "rol_Id": 4,
  "nombre": "Roberto",
  "primer_apellido": "Martinez",
  "segundo_apellido": "Lopez",
  "direccion": "Av. Central 456",
  "correo_electronico": "roberto@example.com",
  "numero_telefono": "9876543210",
  "contrasena": "pass123",
  "estado": true,
  "fecha_registro": "2026-03-06T09:00:00",
  "fecha_actualizacion": "2026-03-06T09:00:00"
}
→ Devuelve: usuario_ID = 1
```

### Paso 2: Crear usuario cajero
```json
POST /usuario/
{
  "rol_Id": 2,
  "nombre": "Ana",
  "primer_apellido": "Lopez",
  "segundo_apellido": "Ramirez",
  "direccion": "Calle Norte 789",
  "correo_electronico": "ana@example.com",
  "numero_telefono": "1234567891",
  "contrasena": "pass123",
  "estado": true,
  "fecha_registro": "2026-03-06T09:00:00",
  "fecha_actualizacion": "2026-03-06T09:00:00"
}
→ Devuelve: usuario_ID = 2
```

### Paso 3: Crear usuario operativo
```json
POST /usuario/
{
  "rol_Id": 3,
  "nombre": "Carlos",
  "primer_apellido": "Gomez",
  "segundo_apellido": "Perez",
  "direccion": "Calle Sur 321",
  "correo_electronico": "carlos@example.com",
  "numero_telefono": "1234567892",
  "contrasena": "pass123",
  "estado": true,
  "fecha_registro": "2026-03-06T09:00:00",
  "fecha_actualizacion": "2026-03-06T09:00:00"
}
→ Devuelve: usuario_ID = 3
```

### Paso 4: Crear servicio
```json
POST /services/
{
  "nombre": "Lavado Completo",
  "descripcion": "Lavado exterior e interior",
  "costo": 150.00,
  "duracion_minutos": 30,
  "estado": true,
  "fecha_registro": "2026-03-06T09:00:00",
  "fecha_actualizacion": "2026-03-06T09:00:00"
}
→ Devuelve: servicio_ID = 1
```

### Paso 5: Registrar vehículo del cliente
```json
POST /autos/
{
  "usuario_Id": 1,
  "placa": "XYZ-5678",
  "marca": "Honda",
  "modelo": "Civic",
  "serie": "2HGES16534H592611",
  "color": "Rojo",
  "tipo": "Sedán",
  "anio": "2022",
  "estado": true,
  "fecha_registro": "2026-03-06T09:00:00",
  "fecha_actualizacion": "2026-03-06T09:00:00"
}
→ Devuelve: vehiculo_ID = 1
```

### Paso 6: Registrar auto-servicio
```json
POST /auto-servicio/
{
  "vehiculo_Id": 1,
  "cajero_Id": 2,
  "operativo_Id": 3,
  "servicio_Id": 1,
  "fecha": "2026-03-06",
  "hora": "10:30:00",
  "estatus": "completado",
  "estado": true,
  "fecha_registro": "2026-03-06T10:00:00",
  "fecha_actualizacion": "2026-03-06T11:00:00"
}
→ Devuelve: auto_servicio_ID = 1
```

### Paso 7: Generar reporte con descuento
```
GET /reporte/1?descuento=20
```

**Respuesta del reporte:**
```json
{
  "success": true,
  "data": {
    "id_servicio_vehiculo": 1,
    "cliente_vehiculo": {
      "cliente_id": 1,
      "cliente_nombre": "Roberto Martinez Lopez",
      "vehiculo_id": 1,
      "vehiculo_placa": "XYZ-5678",
      "vehiculo_marca": "Honda",
      "vehiculo_modelo": "Civic",
      "vehiculo_color": "Rojo"
    },
    "servicio": {
      "servicio_id": 1,
      "servicio_nombre": "Lavado Completo",
      "servicio_costo": 150.00
    },
    "operativo": {
      "usuario_id": 3,
      "usuario_nombre": "Carlos Gomez Perez"
    },
    "cajero": {
      "usuario_id": 2,
      "usuario_nombre": "Ana Lopez Ramirez"
    },
    "descuento": 20.00,
    "total": 130.00,
    "fecha_servicio": "2026-03-06",
    "hora_servicio": "10:30:00"
  },
  "message": "Reporte generado exitosamente"
}
```
pruebaa
{
  "vehiculo_Id": 1,
  "cajero_Id": 1,
  "operativo_Id": 1,
  "servicio_Id": 1,
  "fecha": "2026-03-10",
  "hora": "10:30:00",
  "estatus": "completado",
  "estado": true,
  "fecha_registro": "2026-03-10T02:18:00.000Z",
  "fecha_actualizacion": "2026-03-10T02:18:00.000Z"
}
git