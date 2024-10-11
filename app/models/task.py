from app import db

# Tabla intermedia para la relación de muchos a muchos entre Tareas y Categorías
task_category = db.Table('task_category',
    db.Column('task_id', db.Integer, db.ForeignKey('tasks.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
)

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    completed = db.Column(db.Boolean, default=False, nullable=False)

    # Relación con Categorías (muchos a muchos)
    categories = db.relationship('Category', secondary=task_category, backref=db.backref('tasks', lazy=True))

    def __init__(self, title, description=None, completed=False):
        self.title = title
        self.description = description
        self.completed = completed
