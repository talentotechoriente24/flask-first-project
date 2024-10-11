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
    @jwt_required()
    @category_ns.marshal_list_with(category_response_model)  # Decorador para definir el formato de la respuesta
    def get(self):
        """Obtener todas las categorías"""
        categories = CategoryService.get_all_categories()
        return categories, 200

    @category_ns.expect(category_model, validate=True)
    @jwt_required()
    @category_ns.marshal_with(category_response_model, code=201)  # Decorador para definir el formato de la respuesta
    def post(self):
        """Crear una nueva categoría (Solo para administradores)"""
        data = request.get_json()
        category = CategoryService.create_category(data['name'])
        return category, 201
