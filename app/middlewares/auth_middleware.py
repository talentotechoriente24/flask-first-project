from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import jsonify
from app.services.user_service import UserService

def role_required(required_role):
    """
    Middleware personalizado para verificar si el usuario autenticado tiene un rol específico.
    
    Args:
        required_role (str): El rol requerido que el usuario debe tener para acceder al recurso.
    
    Returns:
        Función decoradora que protege el endpoint y restringe el acceso si el usuario no tiene el rol adecuado.
    """
    
    def decorator(func):
        @wraps(func)  # Mantiene el nombre y la docstring original de la función decorada
        def wrapper(*args, **kwargs):
            # Obtener el nombre de usuario (identity) del token JWT actual
            username = get_jwt_identity()
            
            # Buscar el usuario en la base de datos por su nombre de usuario
            user = UserService.get_user_by_username(username)
            
            # Verificar si el rol del usuario coincide con el rol requerido
            if user.role.name != required_role:
                # Si el usuario no tiene el rol adecuado, se retorna un mensaje de error y un código de estado 403
                return jsonify({"message": "Acceso denegado"}), 403
            
            # Si el rol es correcto, continuar con la ejecución del endpoint
            return func(*args, **kwargs)
        
        return wrapper  # Retorna la función decorada con las verificaciones de rol
    return decorator  # Retorna el decorador

