from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar las extensiones
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

     # Configuración del autorizador JWT para Swagger
    authorizations = {
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'JWT Bearer token. Ejemplo: "Bearer {token}"'
        }
    }

    # Crear la API de Flask-RESTX con el autorizador JWT
    api = Api(app, 
              title='API de Usuarios y Tareas', 
              version='1.0', 
              description='API para gestión de usuarios, tareas, y roles',
              authorizations=authorizations,  # Agregar autorizaciones a la API
              security='Bearer'  # Definir el esquema de seguridad predeterminado
    )

    # Importar y registrar los blueprints (namespaces)
    from .controllers.user_controller import user_ns
    from .controllers.auth_controller import auth_ns
    from .controllers.role_controller import role_ns
    from .controllers.task_controller import task_ns
    from .controllers.category_controller import category_ns

    # Registrar los namespaces en la API
    api.add_namespace(user_ns, path='/users')
    api.add_namespace(auth_ns, path='/auth')
    api.add_namespace(role_ns, path='/roles')
    api.add_namespace(task_ns, path='/tasks')
    api.add_namespace(category_ns, path='/categories')

    return app
