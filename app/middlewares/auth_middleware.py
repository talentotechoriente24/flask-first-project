from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import jsonify
from app.services.user_service import UserService

def role_required(required_role):
    """Middleware para verificar si el usuario tiene el rol requerido"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            username = get_jwt_identity()
            user = UserService.get_user_by_username(username)
            if user.role.name != required_role:
                return jsonify({"message": "Acceso denegado"}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator
