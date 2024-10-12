from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.user_service import UserService
from flask_jwt_extended import create_access_token
from app import bcrypt

# Crear un espacio de nombres (namespace) para la autenticación
auth_ns = Namespace('auth', description='Operaciones de autenticación')

# Definir el modelo de autenticación para la documentación de Swagger
auth_model = auth_ns.model('Auth', {
    'username': fields.String(required=True, description='Nombre de usuario'),  # Campo requerido: nombre de usuario
    'password': fields.String(required=True, description='Contraseña'),         # Campo requerido: contraseña
})

# Definir el controlador de autenticación
@auth_ns.route('/login')
class AuthResource(Resource):
    @auth_ns.doc('login_user')  # Documentar el endpoint en Swagger
    @auth_ns.expect(auth_model, validate=True)  # Esperar el modelo de autenticación en la solicitud y validarlo
    def post(self):
        """Iniciar sesión y obtener un token JWT"""
        # Obtener los datos enviados en el cuerpo de la solicitud en formato JSON
        data = request.get_json()
        
        # Buscar al usuario en la base de datos según el nombre de usuario proporcionado
        user = UserService.get_user_by_username(data['username'])
        
        # Verificar si el usuario existe y si la contraseña es correcta usando bcrypt
        if user and bcrypt.check_password_hash(user.password, data['password']):
            # Si la autenticación es correcta, generar un token JWT
            access_token = create_access_token(identity=user.username)
            
            # Devolver el token JWT como respuesta en formato JSON
            return jsonify({'access_token': access_token})
        
        # Si la autenticación falla (usuario no encontrado o contraseña incorrecta), devolver un error 401
        return jsonify({'message': 'Invalid credentials'}), 401
