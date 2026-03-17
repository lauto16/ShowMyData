# ShowMyData

Aplicación simple para subir, listar y eliminar archivos con autenticación básica por contraseña.

---

## Requisitos

* Python 3.10+
* Node.js 18+
* npm o yarn

---

# Backend
Ingresar a la carpeta llamada "backend"

## 1. Crear entorno virtual

```bash
pip install virtualenv
```

```bash
python -m virtualenv venv 
```

### Activar entorno

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / Mac:**

```bash
source venv/bin/activate
```

---

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```


## 3: Ejecutar script para agregar contraseña inicial:

```bash
python initial_config.py
```

Servidor disponible en:
[http://localhost:8000](http://localhost:8000)

---

# Frontend (React + Vite)
# Ingresar a la carpeta "frontend"

## 1. Instalar dependencias

```bash
npm install
```

---

# Ingresar a la carpeta "show-my-data"
## 2. Instalar dependencias

```bash
npm install
```

---

Frontend disponible en:
[http://localhost:5173](http://localhost:5173)

---

## Iniciar servicio:
Doble click al archivo start_app.bat dentro de "show_my_data"

## Funcionalidades

* Subir archivos
* Listar archivos
* Buscar archivos
* Seleccionar múltiples
* Eliminar archivos seleccionados

---

## Notas importantes

* La autenticación es básica (sin JWT)
* No hay protección real de endpoints
* Las contraseñas se guardan en texto plano
