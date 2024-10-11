# app/services/role_service.py
from app.models.role import Role

class RoleService:
    @staticmethod
    def create_role(name):
        """Crear un nuevo rol en la base de datos"""
        from app import db  # Importamos db dentro de la función
        role = Role.query.filter_by(name=name).first()
        if role:
            raise ValueError("Role already exists")
        new_role = Role(name=name)
        db.session.add(new_role)
        db.session.commit()
        return new_role

    @staticmethod
    def get_all_roles():
        """Obtener todos los roles disponibles"""
        return Role.query.all()

    @staticmethod
    def get_role_by_id(role_id):
        """Obtener un rol por su ID"""
        return Role.query.get(role_id)
