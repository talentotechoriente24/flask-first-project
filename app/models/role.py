from app import db

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)  # Esta es la clave primaria que debe referenciar User
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name
