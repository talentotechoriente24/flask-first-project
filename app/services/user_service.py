from app import db, bcrypt
from app.models.user import User
from app.models.role import Role

class UserService:
    @staticmethod
    def create_user(username, password, role_id):
        """
        Crear un nuevo usuario con un rol asignado.
        
        Args:
            username (str): Nombre de usuario del nuevo usuario.
            password (str): Contraseña en texto plano que será encriptada.
            role_id (int): ID del rol que se asociará al usuario.
        
        Returns:
            User: El usuario creado.
        
        Raises:
            ValueError: Si el rol no es encontrado.
        """
        # Buscar el rol asociado al usuario por su ID
        role = Role.query.filter_by(id=role_id).first()
        if not role:
            # Si no se encuentra el rol, lanzar una excepción
            raise ValueError('Role not found')

        # Generar un hash seguro de la contraseña con bcrypt
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        # Crear un nuevo objeto User con la contraseña hasheada y el rol asociado
        user = User(username=username, password=hashed_password, role_id=role.id)
        
        # Añadir el nuevo usuario a la base de datos
        db.session.add(user)
        db.session.commit()
        
        return user  # Retornar el usuario recién creado
    
    @staticmethod
    def get_all_users():
        """
        Obtener todos los usuarios de la base de datos.
        
        Returns:
            List[User]: Lista de todos los usuarios en la base de datos.
        """
        # Recuperar todos los registros de la tabla User
        return User.query.all()

    @staticmethod
    def get_user_by_username(username):
        """
        Obtener un usuario por su nombre de usuario.
        
        Args:
            username (str): Nombre de usuario a buscar.
        
        Returns:
            User: El usuario encontrado o None si no existe.
        """
        # Filtrar usuarios por su nombre de usuario (username)
        return User.query.filter_by(username=username).first()

    @staticmethod
    def update_user(username, new_data):
        """
        Actualizar los datos de un usuario existente.
        
        Args:
            username (str): Nombre del usuario a actualizar.
            new_data (dict): Diccionario con los nuevos datos, como 'password' o 'role'.
        
        Returns:
            None
        
        Raises:
            ValueError: Si el usuario no es encontrado.
        """
        # Buscar al usuario por su nombre de usuario
        user = UserService.get_user_by_username(username)
        if not user:
            # Si no se encuentra el usuario, lanzar una excepción
            raise ValueError('User not found')

        # Si se proporciona una nueva contraseña, generar el hash
        if 'password' in new_data:
            user.password = bcrypt.generate_password_hash(new_data['password']).decode('utf-8')

        # Si se proporciona un nuevo rol, buscarlo por su ID
        if 'role' in new_data:
            role = Role.query.filter_by(id=new_data['role']).first()
            if role:
                user.role = role  # Asignar el nuevo rol si es válido

        # Guardar los cambios en la base de datos
        db.session.commit()

    @staticmethod
    def delete_user(username):
        """
        Eliminar un usuario existente.
        
        Args:
            username (str): Nombre del usuario a eliminar.
        
        Returns:
            None
        
        Raises:
            ValueError: Si el usuario no es encontrado.
        """
        # Buscar al usuario por su nombre de usuario
        user = UserService.get_user_by_username(username)
        if not user:
            # Si no se encuentra el usuario, lanzar una excepción
            raise ValueError('User not found')

        # Eliminar el usuario de la base de datos
        db.session.delete(user)
        db.session.commit()
