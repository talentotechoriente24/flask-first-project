from app import db
from app.models.role import Role

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)  # Clave foránea hacia la tabla 'roles'

    role = db.relationship('Role', backref='users')  # Relación con el modelo Role

    def __init__(self, username, password, role_id):
        self.username = username
        self.password = password
        self.role_id = role_id
