from app import db

class Role(db.Model):
    """
    Modelo que representa un rol en el sistema.

    Cada rol define un conjunto de permisos o acciones que un usuario puede realizar.
    Este modelo está relacionado con los usuarios para determinar qué rol tiene cada usuario.

    Atributos:
        id (int): Identificador único del rol (clave primaria).
        name (str): Nombre del rol, que debe ser único (ej: 'admin', 'user').

    """
    
    __tablename__ = 'roles'  # Nombre de la tabla en la base de datos

    # Definición de columnas de la tabla
    id = db.Column(db.Integer, primary_key=True)  # Clave primaria de la tabla
    name = db.Column(db.String(50), unique=True, nullable=False)  # El nombre del rol, debe ser único y no nulo

    def __init__(self, name):
        """
        Constructor de la clase Role.
        
        Args:
            name (str): El nombre del rol (ej: 'admin', 'user').
        """
        self.name = name
