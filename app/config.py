import os
from dotenv import load_dotenv

# Cargar el archivo .env en las variables de entorno
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@{os.environ.get('DB_HOST')}/{os.environ.get('DB_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_key'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt_super_secret_key'
