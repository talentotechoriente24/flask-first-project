from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.user_service import UserService

# Crear un espacio de nombres (namespace) para los usuarios
user_ns = Namespace('users', description='Operaciones relacionadas con los usuarios')

# Definir el modelo de usuario para la documentación de Swagger
user_model = user_ns.model('User', {
    'username': fields.String(required=True, description='Nombre de usuario'),
    'password': fields.String(required=True, description='Contraseña'),
    'role': fields.String(required=True, description='Rol del usuario'),
})

# Definir el controlador de usuarios con decoradores para la documentación
@user_ns.route('/')
class UserResource(Resource):
    @user_ns.doc('create_user')
    @user_ns.expect(user_model, validate=True)  # Decorador para esperar el modelo en la petición
    def post(self):
        """
        Crear un nuevo usuario
        ---
        Este método permite crear un nuevo usuario proporcionando el nombre de usuario, la contraseña y el rol.
        
        Body Parameters:
        - username: El nombre del usuario a crear.
        - password: La contraseña del usuario.
        - role: El rol asignado al usuario (por ejemplo, admin, user).

        Responses:
        - 201: Usuario creado con éxito.
        - 400: Si ocurre un error durante la creación del usuario.
        """
        data = request.get_json()  # Obtiene los datos en formato JSON del cuerpo de la solicitud
        user = UserService.create_user(data['username'], data['password'], data['role'])
        # Usamos jsonify para asegurarnos de que la respuesta siga el formato JSON válido.
        return jsonify({'message': 'User created successfully', 'user': user.username})

    @user_ns.doc('get_users')
    def get(self):
        """
        Obtener todos los usuarios
        ---
        Este método permite obtener una lista de todos los usuarios registrados en la base de datos.

        Responses:
        - 200: Retorna una lista de nombres de usuarios.
        """
        users = UserService.get_all_users()  # Llama al servicio para obtener todos los usuarios
        # Usamos jsonify para garantizar que la lista de usuarios se retorne como un JSON válido.
        return jsonify({'users': [user.username for user in users]})  # Retorna solo los nombres de usuario


@user_ns.route('/<username>')
@user_ns.param('username', 'El nombre del usuario')
class UserDetailResource(Resource):
    @user_ns.doc('delete_user')
    def delete(self, username):
        """
        Eliminar un usuario
        ---
        Este método permite eliminar un usuario existente basado en el nombre de usuario.

        Path Parameters:
        - username: El nombre del usuario a eliminar.

        Responses:
        - 200: Usuario eliminado con éxito.
        - 404: Si el usuario no se encuentra.
        """
        UserService.delete_user(username)  # Llama al servicio para eliminar al usuario
        # Usamos jsonify para enviar un mensaje de éxito en formato JSON.
        return jsonify({'message': 'User deleted successfully'})

    @user_ns.doc('update_user')
    @user_ns.expect(user_model, validate=True)
    def put(self, username):
        """
        Actualizar un usuario
        ---
        Este método permite actualizar la información de un usuario basado en su nombre de usuario.

        Path Parameters:
        - username: El nombre del usuario que se actualizará.

        Body Parameters:
        - username: El nuevo nombre de usuario (opcional).
        - password: La nueva contraseña (opcional).
        - role: El nuevo rol (opcional).

        Responses:
        - 200: Usuario actualizado con éxito.
        - 404: Si el usuario no se encuentra.
        """
        new_data = request.get_json()  # Obtiene los nuevos datos para la actualización
        UserService.update_user(username, new_data)  # Llama al servicio para actualizar el usuario
        # Usamos jsonify para enviar un mensaje de éxito en formato JSON.
        return jsonify({'message': 'User updated successfully'})

