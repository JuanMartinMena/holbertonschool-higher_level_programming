from flask import Flask, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

# Secret key for JWT
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

# In-memory user data
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

### 1. Basic Authentication Setup

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

### 2. JWT Authentication Setup

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return "Bad username or password", 401

    access_token = create_access_token(identity={'username': username, 'role': user['role']})
    return f'{{"access_token": "{access_token}"}}'

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

### 3. Role-based Access Control

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return '{"error": "Admin access required"}', 403
    return "Admin Access: Granted"

### 4. Custom JWT Error Handlers

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return '{"error": "Missing or invalid token"}', 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return '{"error": "Invalid token"}', 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return '{"error": "Token has expired"}', 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return '{"error": "Token has been revoked"}', 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return '{"error": "Fresh token required"}', 401

if __name__ == '__main__':
    app.run(debug=True)
