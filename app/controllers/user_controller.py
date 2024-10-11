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
        """Crear un nuevo usuario"""
        data = request.get_json()
        user = UserService.create_user(data['username'], data['password'], data['role'])
        return jsonify({'message': 'User created successfully', 'user': user.username})

    @user_ns.doc('get_users')
    def get(self):
        """Obtener todos los usuarios (este es un ejemplo)"""
        users = UserService.get_all_users()
        return jsonify({'users': [user.username for user in users]})

@user_ns.route('/<username>')
@user_ns.param('username', 'El nombre del usuario')
class UserDetailResource(Resource):
    @user_ns.doc('delete_user')
    def delete(self, username):
        """Eliminar un usuario por su nombre"""
        UserService.delete_user(username)
        return jsonify({'message': 'User deleted successfully'})
