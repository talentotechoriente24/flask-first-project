from app import db
from app.models.category import Category

class CategoryService:
    """Servicio que gestiona las operaciones CRUD para las categorías"""

    @staticmethod
    def create_category(name):
        """Crear una nueva categoría en la base de datos.
        
        Args:
            name (str): El nombre de la categoría a crear.

        Returns:
            Category: La nueva categoría creada.

        Raises:
            ValueError: Si la categoría ya existe.
        """
        # Verificar si la categoría con el mismo nombre ya existe
        category = Category.query.filter_by(name=name).first()
        if category:
            # Si ya existe una categoría con el mismo nombre, se lanza una excepción
            raise ValueError("Category already exists")
        
        # Si no existe, crear una nueva instancia de Category
        new_category = Category(name=name)
        
        # Guardar la nueva categoría en la base de datos
        db.session.add(new_category)
        db.session.commit()
        
        return new_category

    @staticmethod
    def update_category(category_id, name):
        """Actualizar una categoría existente en la base de datos.
        
        Args:
            category_id (int): El ID de la categoría a actualizar.
            name (str): El nuevo nombre de la categoría.

        Returns:
            Category: La categoría actualizada.

        Raises:
            ValueError: Si la categoría no se encuentra.
        """
        # Buscar la categoría por su ID
        category = Category.query.get(category_id)
        if not category:
            # Si la categoría no se encuentra, lanzar una excepción
            raise ValueError('Category not found')
        
        # Actualizar el nombre de la categoría
        category.name = name
        
        # Guardar los cambios en la base de datos
        db.session.commit()
        
        return category

    @staticmethod
    def delete_category(category_id):
        """Eliminar una categoría existente de la base de datos.
        
        Args:
            category_id (int): El ID de la categoría a eliminar.

        Raises:
            ValueError: Si la categoría no se encuentra.
        """
        # Buscar la categoría por su ID
        category = Category.query.get(category_id)
        if not category:
            # Si la categoría no se encuentra, lanzar una excepción
            raise ValueError('Category not found')
        
        # Eliminar la categoría de la base de datos
        db.session.delete(category)
        db.session.commit()

    @staticmethod
    def get_all_categories():
        """Obtener todas las categorías disponibles en la base de datos.
        
        Returns:
            List[Category]: Una lista de todas las categorías.
        """
        # Devuelve todas las categorías usando una consulta SQLAlchemy
        return Category.query.all()

    @staticmethod
    def serialize_category(category):
        """Convierte un objeto Category en un diccionario serializable.
        
        Args:
            category (Category): La instancia de Category que se desea serializar.

        Returns:
            dict: Un diccionario con la estructura de la categoría serializada.
        """
        # Devuelve un diccionario con el ID y el nombre de la categoría
        return {'id': category.id, 'name': category.name}
