from app import db
from app.models.role import Role
from app.models.user import User  # Asegúrate de tener el modelo User importado

class RoleService:
    """Servicio para manejar las operaciones CRUD y adicionales para roles."""

    @staticmethod
    def create_role(name):
        """Crear un nuevo rol en la base de datos.
        
        Args:
            name (str): El nombre del nuevo rol.

        Returns:
            Role: El nuevo rol creado.

        Raises:
            ValueError: Si el rol ya existe.
        """
        # Verificar si el rol ya existe
        role = Role.query.filter_by(name=name).first()
        if role:
            raise ValueError("Role already exists")
        
        # Crear un nuevo rol
        new_role = Role(name=name)
        
        # Guardar el rol en la base de datos
        db.session.add(new_role)
        db.session.commit()
        
        return new_role

    @staticmethod
    def get_all_roles():
        """Obtener todos los roles disponibles.
        
        Returns:
            List[Role]: Lista de todos los roles en la base de datos.
        """
        # Retorna todos los roles
        return Role.query.all()

    @staticmethod
    def get_role_by_id(role_id):
        """Obtener un rol por su ID.
        
        Args:
            role_id (int): El ID del rol.

        Returns:
            Role: El rol correspondiente al ID, o None si no existe.
        """
        # Buscar el rol por su ID
        return Role.query.get(role_id)

    @staticmethod
    def update_role(role_id, new_name):
        """Actualizar el nombre de un rol existente.
        
        Args:
            role_id (int): El ID del rol a actualizar.
            new_name (str): El nuevo nombre para el rol.

        Returns:
            Role: El rol actualizado.

        Raises:
            ValueError: Si el rol no se encuentra.
        """
        # Buscar el rol por su ID
        role = Role.query.get(role_id)
        if not role:
            raise ValueError("Role not found")
        
        # Actualizar el nombre del rol
        role.name = new_name
        
        # Confirmar los cambios en la base de datos
        db.session.commit()
        
        return role

    @staticmethod
    def delete_role(role_id):
        """Eliminar un rol existente de la base de datos.
        
        Args:
            role_id (int): El ID del rol a eliminar.

        Raises:
            ValueError: Si el rol no se encuentra.
        """
        # Buscar el rol por su ID
        role = Role.query.get(role_id)
        if not role:
            raise ValueError("Role not found")
        
        # Eliminar el rol
        db.session.delete(role)
        db.session.commit()

    @staticmethod
    def get_users_by_role(role_id):
        """Obtener una lista de usuarios que tienen asignado un rol específico.
        
        Args:
            role_id (int): El ID del rol para buscar los usuarios asociados.

        Returns:
            List[dict]: Lista de diccionarios con los nombres de usuario de los usuarios que tienen asignado el rol.
        
        Raises:
            ValueError: Si el rol no se encuentra.
        """
        # Buscar el rol por su ID
        role = Role.query.get(role_id)
        if not role:
            raise ValueError("Role not found")
        
        # Obtener los usuarios asociados al rol
        users = User.query.filter_by(role_id=role.id).all()
        
        # Retornar una lista de nombres de usuario
        return [{'username': user.username} for user in users]
