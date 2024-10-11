from app import db, bcrypt
from app.models.user import User
from app.models.role import Role

class UserService:
    @staticmethod
    def create_user(username, password, role_id):
        """Crear un nuevo usuario con el rol asociado"""
        # Buscar el rol por ID, no por nombre
        role = Role.query.filter_by(id=role_id).first()
        if not role:
            raise ValueError('Role not found')

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, password=hashed_password, role_id=role.id)  # Asignar el ID del rol
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def get_all_users():
        """Obtener todos los usuarios"""
        return User.query.all()

    @staticmethod
    def get_user_by_username(username):
        """Obtener un usuario por su nombre de usuario"""
        return User.query.filter_by(username=username).first()

    @staticmethod
    def update_user(username, new_data):
        """Actualizar la información del usuario"""
        user = UserService.get_user_by_username(username)
        if not user:
            raise ValueError('User not found')

        if 'password' in new_data:
            user.password = bcrypt.generate_password_hash(new_data['password']).decode('utf-8')

        if 'role' in new_data:
            role = Role.query.filter_by(id=new_data['role']).first()  # Buscar el rol por ID
            if role:
                user.role = role

        db.session.commit()

    @staticmethod
    def delete_user(username):
        """Eliminar un usuario"""
        user = UserService.get_user_by_username(username)
        if not user:
            raise ValueError('User not found')

        db.session.delete(user)
        db.session.commit()
