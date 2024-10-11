# Flask API Project

Este proyecto es una API construida con **Flask**, **Flask-RESTX**, **SQLAlchemy** y autenticación JWT. A continuación se describe cómo clonar el repositorio, configurar el entorno virtual, instalar dependencias, configurar la base de datos, ejecutar migraciones y correr la aplicación.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

- **Python 3.8+**
- **Git**
- **MySQL** (o tu motor de base de datos preferido)
  
### Clonar el Repositorio

1. Abre tu terminal o consola y navega a la carpeta donde deseas clonar el proyecto.
   
2. Ejecuta el siguiente comando para clonar el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
   ```

3. Navega a la carpeta del proyecto:

   ```bash
   cd tu-repo
   ```

### Crear y Activar el Entorno Virtual

1. **Crear el entorno virtual**: Ejecuta el siguiente comando para crear un entorno virtual en Python (dentro del directorio del proyecto):

   - En **Windows**:

     ```bash
     python -m venv venv
     ```

   - En **Linux/MacOS**:

     ```bash
     python3 -m venv venv
     ```

2. **Activar el entorno virtual**:

   - En **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - En **Linux/MacOS**:

     ```bash
     source venv/bin/activate
     ```

3. Verifica que el entorno esté activado. Deberías ver el prefijo `(venv)` en tu consola.

### Instalar las Dependencias

Con el entorno virtual activado, instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

Esto instalará todos los paquetes listados en el archivo `requirements.txt`.

### Configurar la Base de Datos

1. **Crear la base de datos en MySQL**:

   Abre tu consola MySQL o cliente preferido y crea una base de datos:

   ```sql
   CREATE DATABASE flask_api_db;
   ```

2. **Configurar las variables de entorno**:

   Asegúrate de que tienes un archivo `.env` en la raíz del proyecto con las siguientes variables (puedes copiar y pegar desde este ejemplo):

   ```bash
   DB_USER=root
   DB_PASS=root_password
   DB_NAME=flask_api_db
   DB_HOST=localhost
   SECRET_KEY=secret_key
   JWT_SECRET_KEY=jwt_secret_key
   ```

   - Cambia los valores según las credenciales de tu base de datos.
   
   **Nota**: Si no tienes el archivo `.env`, crea uno nuevo en el directorio raíz del proyecto.

### Ejecutar Migraciones

1. **Inicializar las migraciones** (solo la primera vez):

   ```bash
   flask db init
   ```

2. **Crear las migraciones** basadas en los modelos actuales:

   ```bash
   flask db migrate -m "Initial migration."
   ```

3. **Aplicar las migraciones** para crear las tablas en la base de datos:

   ```bash
   flask db upgrade
   ```

### Ejecutar la Aplicación

Finalmente, puedes ejecutar la aplicación Flask localmente con el siguiente comando:

```bash
python run.py
```

Por defecto, la aplicación se ejecutará en `http://127.0.0.1:5000`.

### Uso de Swagger para Documentación

La API cuenta con documentación interactiva que puedes consultar y probar desde tu navegador accediendo a:

```
http://127.0.0.1:5000/
```

Esta interfaz de Swagger te permitirá interactuar con los endpoints de la API de manera visual.

---

## Notas Adicionales

- **Migraciones**: Cada vez que modifiques los modelos de la base de datos, debes ejecutar `flask db migrate` y `flask db upgrade` para aplicar los cambios.
- **Activar entorno virtual**: Recuerda siempre activar el entorno virtual antes de trabajar en el proyecto.
- **Comandos Útiles**:
  - Crear migraciones: `flask db migrate`
  - Aplicar migraciones: `flask db upgrade`
  - Revisar la documentación interactiva: Visita `http://127.0.0.1:5000/` después de ejecutar la aplicación.