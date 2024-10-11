from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.task_service import TaskService
from flask_jwt_extended import jwt_required

# Namespace para Tareas
task_ns = Namespace('tasks', description='Operaciones con las tareas')

# Modelo de entrada para tareas
task_model = task_ns.model('Task', {
    'title': fields.String(required=True, description='Título de la tarea'),
    'description': fields.String(description='Descripción de la tarea'),
    'category_ids': fields.List(fields.Integer, description='IDs de las categorías asociadas')
})

# Modelo de salida para tareas (respuesta)
task_response_model = task_ns.model('TaskResponse', {
    'id': fields.Integer(description='ID de la tarea'),
    'title': fields.String(description='Título de la tarea'),
    'description': fields.String(description='Descripción de la tarea'),
    'completed': fields.Boolean(description='Estado de la tarea (completada o no)'),
    'categories': fields.List(fields.Nested(task_ns.model('Category', {
        'id': fields.Integer(description='ID de la categoría'),
        'name': fields.String(description='Nombre de la categoría')
    })), description='Lista de categorías asociadas a la tarea')
})

@task_ns.route('/')
class TaskListResource(Resource):
    @jwt_required()
    @task_ns.marshal_list_with(task_response_model)  # Serialización automática de la lista de tareas
    def get(self):
        """Obtener todas las tareas"""
        tasks = TaskService.get_all_tasks()
        return tasks, 200

    @task_ns.expect(task_model, validate=True)
    @jwt_required()
    @task_ns.marshal_with(task_response_model, code=201)  # Serialización automática de la tarea creada
    def post(self):
        """Crear una nueva tarea"""
        data = request.get_json()
        task = TaskService.create_task(data['title'], data['description'], data['category_ids'])
        return task, 201 
