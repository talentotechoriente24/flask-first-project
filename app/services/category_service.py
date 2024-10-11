from app import db
from app.models.category import Category

class CategoryService:
    @staticmethod
    def create_category(name):
        """Crear una nueva categoría"""
        category = Category.query.filter_by(name=name).first()
        if category:
            raise ValueError("Category already exists")
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        return new_category

    @staticmethod
    def update_category(category_id, name):
        """Actualizar una categoría"""
        category = Category.query.get(category_id)
        if not category:
            raise ValueError('Category not found')
        category.name = name
        db.session.commit()
        return category

    @staticmethod
    def delete_category(category_id):
        """Eliminar una categoría"""
        category = Category.query.get(category_id)
        if not category:
            raise ValueError('Category not found')
        db.session.delete(category)
        db.session.commit()

    @staticmethod
    def get_all_categories():
        """Obtener todas las categorías"""
        return Category.query.all()

    @staticmethod
    def serialize_category(category):
        """Convierte un objeto Category en un diccionario serializable"""
        return {'id': category.id, 'name': category.name}
