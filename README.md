# K365 Backend - Etapa 1

Backend RESTful para una aplicación web SPA de kiosco inspirada en K365.

Esta primera etapa cumple con los puntos pedidos por la consigna:

- Listar productos disponibles.
- Agregar productos al carrito.
- Eliminar productos del carrito.
- Calcular el total de la compra.
- Persistencia inicial en memoria, sin base de datos.
- Documentación de APIs con Swagger/OpenAPI.
- Tests unitarios de los endpoints principales.

---

## Tecnologías utilizadas

- Python 3
- Flask
- Swagger/OpenAPI
- Pytest

La elección de Flask se hizo porque permite construir APIs REST de forma simple, clara y alineada con los temas vistos en la cursada.

---

## Estructura del proyecto

```text
k365-backend-etapa1/
│
├── app/
│   ├── __init__.py
│   ├── data/
│   │   └── products.py
│   ├── routes/
│   │   ├── cart.py
│   │   ├── health.py
│   │   └── products.py
│   └── services/
│       └── cart_service.py
│
├── docs/
│   └── openapi.yaml
│
├── tests/
│   └── test_api.py
│
├── run.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
cd k365-backend-etapa1
```

Si todavía no subiste el proyecto a GitHub, entrá manualmente a la carpeta donde tengas estos archivos.

---

### 2. Crear entorno virtual

En Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación del entorno virtual, ejecutar:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Después volver a activar:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecutar el servidor

```bash
python run.py
```

La API queda disponible en:

```text
http://127.0.0.1:5000
```

---

## Documentación Swagger

Con el servidor levantado, abrir en el navegador:

```text
http://127.0.0.1:5000/docs
```

También se puede ver el archivo OpenAPI en:

```text
http://127.0.0.1:5000/openapi.yaml
```

---

## Endpoints principales

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/api/health` | Verifica que el servidor esté funcionando |
| GET | `/api/products` | Lista productos disponibles |
| GET | `/api/products/{product_id}` | Obtiene un producto por ID |
| GET | `/api/cart` | Consulta el carrito actual |
| POST | `/api/cart/items` | Agrega un producto al carrito |
| DELETE | `/api/cart/items/{product_id}` | Elimina un producto del carrito |
| DELETE | `/api/cart` | Vacía el carrito |
| GET | `/api/cart/total` | Calcula el total de la compra |

---

## Ejemplos de uso

### Listar productos

```bash
curl http://127.0.0.1:5000/api/products
```

### Agregar producto al carrito

```bash
curl -X POST http://127.0.0.1:5000/api/cart/items ^
  -H "Content-Type: application/json" ^
  -d "{\"product_id\":1,\"quantity\":2}"
```

En PowerShell también se puede probar con:

```powershell
Invoke-RestMethod -Method Post `
  -Uri "http://127.0.0.1:5000/api/cart/items" `
  -ContentType "application/json" `
  -Body '{"product_id":1,"quantity":2}'
```

### Ver carrito

```bash
curl http://127.0.0.1:5000/api/cart
```

### Calcular total

```bash
curl http://127.0.0.1:5000/api/cart/total
```

### Eliminar producto del carrito

```bash
curl -X DELETE http://127.0.0.1:5000/api/cart/items/1
```

---

## Ejecutar tests

```bash
python -m pytest -v
```

Los tests validan:

- Que la API esté activa.
- Que se listen productos.
- Que se pueda obtener un producto por ID.
- Que se pueda agregar un producto al carrito.
- Que agregar el mismo producto incremente la cantidad.
- Que se calcule correctamente el total.
- Que se pueda eliminar un producto del carrito.
- Que se pueda vaciar el carrito.
- Que se manejen errores básicos como producto inexistente o cantidad inválida.

---

## Arquitectura elegida

Se eligió una arquitectura simple por capas:

- `routes`: define los endpoints HTTP.
- `services`: contiene la lógica del carrito.
- `data`: contiene los productos disponibles en memoria.
- `docs`: contiene la documentación OpenAPI.
- `tests`: contiene las pruebas unitarias de los endpoints.

Esta estructura permite mantener separado el manejo de rutas, la lógica de negocio y los datos iniciales.

---

## Dificultades y resolución

### Persistencia en memoria

La consigna pide que la primera etapa no use base de datos. Por eso, el carrito se guarda en una variable interna del backend.

Esta solución es suficiente para la Etapa 1, pero tiene una limitación: si el servidor se reinicia, el carrito se pierde.

En la Etapa 2 se reemplazará esta persistencia en memoria por una base de datos.

### Manejo de errores

Se agregaron respuestas claras para casos comunes:

- Producto inexistente.
- Cantidad inválida.
- Stock insuficiente.
- Producto que se intenta eliminar pero no está en el carrito.

---

## Próxima etapa

En la Etapa 2 se agregará:

- Frontend SPA.
- Integración con base de datos.
- Pruebas E2E.
- Deploy en un entorno accesible.
