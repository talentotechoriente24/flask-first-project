from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_migrate import Migrate
from .config import Config

# Inicializamos las extensiones globalmente para luego asociarlas a la app en la función create_app
db = SQLAlchemy()  # Para la interacción con la base de datos usando SQLAlchemy
migrate = Migrate()  # Para gestionar las migraciones de la base de datos
bcrypt = Bcrypt()  # Para el hash y verificación de contraseñas de los usuarios
jwt = JWTManager()  # Para la gestión de tokens JWT en la autenticación

def create_app():
    """Función factory para crear la aplicación Flask y configurar sus componentes."""
    
    # Creamos una instancia de la aplicación Flask
    app = Flask(__name__)
    
    # Cargamos la configuración de la aplicación desde el archivo de configuración
    app.config.from_object(Config)

    # Inicializamos las extensiones con la aplicación
    db.init_app(app)  # Inicializar SQLAlchemy con la app
    bcrypt.init_app(app)  # Inicializar Bcrypt con la app
    jwt.init_app(app)  # Inicializar JWTManager con la app
    migrate.init_app(app, db)  # Inicializar Migrate con la app y la base de datos

    # Autorizador JWT para integrar con la documentación Swagger
    authorizations = {
        'Bearer': {
            'type': 'apiKey',  # Tipo apiKey define que el token JWT se envía en el encabezado de la solicitud
            'in': 'header',  # El token JWT se debe enviar en el encabezado de la solicitud HTTP
            'name': 'Authorization',  # Nombre del campo del encabezado HTTP para el token
            'description': 'JWT Bearer token. Ejemplo: "Bearer {token}"'  # Instrucción sobre cómo enviar el token
        }
    }

    # Configuramos la API Flask-RESTX, que nos ayuda a crear endpoints RESTful con documentación Swagger integrada
    api = Api(
        app,  # La aplicación Flask en la que registramos la API
        title='API de Usuarios y Tareas',  # Título para la documentación Swagger
        version='1.0',  # Versión de la API
        description='API para gestión de usuarios, tareas, y roles',  # Descripción de la API
        authorizations=authorizations,  # Añadimos la configuración de JWT a la API
        security='Bearer'  # Define que los endpoints por defecto usan el esquema de seguridad JWT
    )

    # Importamos los controladores y namespaces que organizan las rutas/endpoints de la API
    from .controllers.user_controller import user_ns  # Controlador para la gestión de usuarios
    from .controllers.auth_controller import auth_ns  # Controlador para la autenticación
    from .controllers.role_controller import role_ns  # Controlador para la gestión de roles
    from .controllers.task_controller import task_ns  # Controlador para la gestión de tareas
    from .controllers.category_controller import category_ns  # Controlador para la gestión de categorías

    # Registramos cada namespace (grupo de rutas) en la API
    api.add_namespace(user_ns, path='/users')  # Registrar el namespace de usuarios en /users
    api.add_namespace(auth_ns, path='/auth')  # Registrar el namespace de autenticación en /auth
    api.add_namespace(role_ns, path='/roles')  # Registrar el namespace de roles en /roles
    api.add_namespace(task_ns, path='/tasks')  # Registrar el namespace de tareas en /tasks
    api.add_namespace(category_ns, path='/categories')  # Registrar el namespace de categorías en /categories

    # Retornamos la aplicación ya configurada
    return app
