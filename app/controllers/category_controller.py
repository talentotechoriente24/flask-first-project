from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.category_service import CategoryService
from flask_jwt_extended import jwt_required

# Crear un espacio de nombres (namespace) para categorías
category_ns = Namespace('categories', description='Operaciones relacionadas con las categorías')

# Definir el modelo de entrada de categoría para la documentación de Swagger
category_model = category_ns.model('Category', {
    'name': fields.String(required=True, description='Nombre de la categoría')
})

# Definir el modelo de salida de categoría para la documentación de Swagger
category_response_model = category_ns.model('CategoryResponse', {
    'id': fields.Integer(description='ID de la categoría'),
    'name': fields.String(description='Nombre de la categoría')
})

@category_ns.route('/')
class CategoryListResource(Resource):
    @jwt_required()  # Requiere autenticación JWT para acceder a este endpoint
    @category_ns.marshal_list_with(category_response_model)  # Serialización automática de la respuesta
    def get(self):
        """Obtener todas las categorías"""
        categories = CategoryService.get_all_categories()  # Llama al servicio para obtener todas las categorías
        return categories, 200  # Retorna la lista de categorías con un código de estado 200 (OK)

    @category_ns.expect(category_model, validate=True)  # Espera los datos de entrada según el modelo de categoría
    @jwt_required()  # Requiere autenticación JWT para acceder a este endpoint
    @category_ns.marshal_with(category_response_model, code=201)  # Serializa la respuesta de la categoría creada
    def post(self):
        """Crear una nueva categoría (Solo para administradores)"""
        data = request.get_json()  # Obtiene los datos de la solicitud en formato JSON
        category = CategoryService.create_category(data['name'])  # Llama al servicio para crear la categoría
        return category, 201  # Retorna la categoría creada con un código de estado 201 (Creado)

@category_ns.route('/<int:category_id>')
@category_ns.param('category_id', 'El ID de la categoría')
class CategoryResource(Resource):
    @jwt_required()  # Requiere autenticación JWT
    @category_ns.marshal_with(category_response_model)
    def get(self, category_id):
        """Obtener una categoría por su ID"""
        category = CategoryService.get_category_by_id(category_id)  # Llama al servicio para obtener la categoría
        if not category:
            return {'message': 'Category not found'}, 404  # Si no se encuentra, retorna un error 404
        return category, 200

    @jwt_required()  # Requiere autenticación JWT
    @category_ns.expect(category_model, validate=True)
    @category_ns.marshal_with(category_response_model)
    def put(self, category_id):
        """Actualizar una categoría existente"""
        data = request.get_json()  # Obtiene los nuevos datos para la categoría
        category = CategoryService.update_category(category_id, data['name'])  # Llama al servicio para actualizar
        return category, 200  # Retorna la categoría actualizada con un código de estado 200 (OK)

    @jwt_required()  # Requiere autenticación JWT
    def delete(self, category_id):
        """Eliminar una categoría por su ID"""
        CategoryService.delete_category(category_id)  # Llama al servicio para eliminar la categoría
        return {'message': 'Category deleted successfully'}, 200  # Retorna un mensaje de confirmación
