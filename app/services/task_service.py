from app import db
from app.models.task import Task
from app.models.category import Category

class TaskService:
    @staticmethod
    def create_task(title, description, category_ids):
        """Crear una nueva tarea con categorías asociadas"""
        categories = Category.query.filter(Category.id.in_(category_ids)).all()
        new_task = Task(title=title, description=description, completed=False)
        new_task.categories = categories
        db.session.add(new_task)
        db.session.commit()
        return new_task

    @staticmethod
    def update_task(task_id, title=None, description=None, completed=None, category_ids=None):
        """Actualizar los detalles de una tarea"""
        task = Task.query.get(task_id)
        if not task:
            raise ValueError('Task not found')
        
        if title:
            task.title = title
        if description:
            task.description = description
        if completed is not None:
            task.completed = completed
        if category_ids:
            categories = Category.query.filter(Category.id.in_(category_ids)).all()
            task.categories = categories

        db.session.commit()
        return task

    @staticmethod
    def delete_task(task_id):
        """Eliminar una tarea"""
        task = Task.query.get(task_id)
        if not task:
            raise ValueError('Task not found')
        db.session.delete(task)
        db.session.commit()

    @staticmethod
    def get_all_tasks():
        """Obtener todas las tareas"""
        return Task.query.all()

    @staticmethod
    def mark_task_completed(task_id):
        """Marcar una tarea como completada"""
        task = Task.query.get(task_id)
        if not task:
            raise ValueError('Task not found')
        task.completed = True
        db.session.commit()

    @staticmethod
    def mark_task_incomplete(task_id):
        """Marcar una tarea como incompleta"""
        task = Task.query.get(task_id)
        if not task:
            raise ValueError('Task not found')
        task.completed = False
        db.session.commit()
