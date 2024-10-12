from app import db
from app.models.role import Role

class User(db.Model):
    """
    Modelo que representa un usuario en el sistema.

    Cada usuario tiene un nombre de usuario, una contraseña encriptada y está asociado con un rol a través de una clave foránea.

    Atributos:
        id (int): Identificador único del usuario (clave primaria).
        username (str): Nombre de usuario, debe ser único.
        password (str): Contraseña encriptada del usuario.
        role_id (int): Clave foránea que referencia al rol asignado al usuario.
        role (Role): Relación con el modelo Role que indica el rol del usuario.
    """
    
    __tablename__ = 'users'  # Especifica el nombre de la tabla en la base de datos

    # Definición de columnas de la tabla
    id = db.Column(db.Integer, primary_key=True)  # Clave primaria de la tabla
    username = db.Column(db.String(80), unique=True, nullable=False)  # Nombre de usuario, debe ser único y no nulo
    password = db.Column(db.String(120), nullable=False)  # Contraseña encriptada del usuario, no puede ser nula
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)  # Clave foránea hacia la tabla 'roles'

    # Relación con el modelo Role
    role = db.relationship('Role', backref='users')  # Define la relación con el modelo Role y permite acceso inverso desde Role a User

    def __init__(self, username, password, role_id):
        """
        Constructor de la clase User.

        Args:
            username (str): El nombre de usuario.
            password (str): La contraseña encriptada.
            role_id (int): El ID del rol asociado.
        """
        self.username = username
        self.password = password
        self.role_id = role_id
