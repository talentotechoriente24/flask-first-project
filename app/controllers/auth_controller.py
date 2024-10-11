from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.user_service import UserService
from flask_jwt_extended import create_access_token
from app import bcrypt

# Crear un espacio de nombres (namespace) para la autenticación
auth_ns = Namespace('auth', description='Operaciones de autenticación')

# Definir el modelo de autenticación para la documentación de Swagger
auth_model = auth_ns.model('Auth', {
    'username': fields.String(required=True, description='Nombre de usuario'),
    'password': fields.String(required=True, description='Contraseña'),
})

# Definir el controlador de autenticación
@auth_ns.route('/login')
class AuthResource(Resource):
    @auth_ns.doc('login_user')
    @auth_ns.expect(auth_model, validate=True)  # Esperar el modelo de autenticación en la solicitud
    def post(self):
        """Iniciar sesión y obtener un token JWT"""
        data = request.get_json()
        user = UserService.get_user_by_username(data['username'])
        if user and bcrypt.check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity=user.username)
            return jsonify({'access_token': access_token})
        return jsonify({'message': 'Invalid credentials'}), 401
