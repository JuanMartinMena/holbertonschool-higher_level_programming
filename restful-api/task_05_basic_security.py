from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from functools import wraps

app = Flask(__name__)
auth = HTTPBasicAuth()

# Clave secreta para JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# Datos de usuarios con contraseñas hash
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Verificación de autenticación básica
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return users[username]
    return None

# Ruta protegida por autenticación básica
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200

# Ruta de login para JWT
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return {"error": "Missing username or password"}, 400

    user = users.get(username, None)
    if user and check_password_hash(user['password'], password):
        # Crear el token JWT
        access_token = create_access_token(identity={"username": username, "role": user["role"]})
        return {"access_token": access_token}, 200
    return {"error": "Invalid credentials"}, 401

# Ruta protegida por JWT
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

# Decorador para requerir que el usuario sea admin
def admin_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        user = get_jwt_identity()
        if user['role'] != 'admin':
            return {"error": "Admin access required"}, 403
        return fn(*args, **kwargs)
    return wrapper

# Ruta solo accesible para administradores
@app.route('/admin-only', methods=['GET'])
@admin_required
def admin_only():
    return "Admin Access: Granted", 200

# Manejadores de errores para JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return {"error": "Missing or invalid token"}, 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return {"error": "Invalid token"}, 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return {"error": "Token has expired"}, 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return {"error": "Token has been revoked"}, 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return {"error": "Fresh token required"}, 401

# Manejador de errores para autenticación básica
@auth.error_handler
def unauthorized():
    return "Unauthorized access", 401

if __name__ == '__main__':
    app.run(debug=True)
