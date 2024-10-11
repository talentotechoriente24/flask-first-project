from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.role_service import RoleService

# Crear un espacio de nombres (namespace) para roles
role_ns = Namespace('roles', description='Operaciones relacionadas con los roles')

# Definir el modelo de entrada de rol para la documentación de Swagger
role_model = role_ns.model('Role', {
    'name': fields.String(required=True, description='Nombre del rol')
})

# Definir el modelo de salida de rol para la documentación de Swagger
role_response_model = role_ns.model('RoleResponse', {
    'id': fields.Integer(description='ID del rol'),
    'name': fields.String(description='Nombre del rol')
})

# Controlador para manejar las operaciones CRUD de roles
@role_ns.route('/')
class RoleListResource(Resource):
    @role_ns.doc('get_roles')
    @role_ns.marshal_list_with(role_response_model)  # Decorador para definir el formato de la respuesta
    def get(self):
        """Obtener todos los roles"""
        roles = RoleService.get_all_roles()
        return roles, 200

    @role_ns.doc('create_role')
    @role_ns.expect(role_model, validate=True)  # Decorador para esperar el modelo en la solicitud
    @role_ns.marshal_with(role_response_model, code=201)  # Decorador para definir el formato de la respuesta
    def post(self):
        """Crear un nuevo rol"""
        data = request.get_json()
        try:
            role = RoleService.create_role(data['name'])
            return role, 201
        except ValueError as e:
            return {'message': str(e)}, 400


@role_ns.route('/<int:role_id>')
@role_ns.param('role_id', 'El ID del rol')
class RoleResource(Resource):
    @role_ns.doc('get_role_by_id')
    @role_ns.marshal_with(role_response_model)
    def get(self, role_id):
        """Obtener un rol por su ID"""
        role = RoleService.get_role_by_id(role_id)
        if not role:
            return {'message': 'Role not found'}, 404
        return role, 200
