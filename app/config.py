import os
from dotenv import load_dotenv

# Cargar el archivo .env en las variables de entorno
load_dotenv()

class Config:
    """
    Clase Config para manejar la configuración de la aplicación Flask.
    
    Carga las variables de entorno desde un archivo .env utilizando `dotenv` y
    configura las opciones de la base de datos, el sistema de autenticación JWT, 
    y otras configuraciones esenciales de Flask.

    Atributos:
        SQLALCHEMY_DATABASE_URI (str): URI para la conexión a la base de datos MySQL.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Deshabilita el seguimiento de modificaciones de objetos en SQLAlchemy para optimizar el rendimiento.
        SQLALCHEMY_ECHO (bool): Activa la impresión de todas las consultas SQL ejecutadas por la aplicación en la consola, útil para depuración.
        SECRET_KEY (str): Clave secreta para firmar cookies y otras funcionalidades de seguridad de Flask.
        JWT_SECRET_KEY (str): Clave secreta utilizada para generar y verificar tokens JWT.
    """

    # URI de conexión a la base de datos MySQL, con las credenciales y el host tomados del archivo .env
    SQLALCHEMY_DATABASE_URI = f"mysql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@{os.environ.get('DB_HOST')}/{os.environ.get('DB_NAME')}"
    
    # Desactiva el rastreo de modificaciones para mejorar el rendimiento de la aplicación
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Activa el logging de las consultas SQL en la consola
    SQLALCHEMY_ECHO = True

    # Clave secreta para funcionalidades de seguridad como sesiones y cookies
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_key'

    # Clave secreta para la autenticación JWT, usada para generar tokens
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt_super_secret_key'
