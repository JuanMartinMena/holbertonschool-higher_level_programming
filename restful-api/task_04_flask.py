from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

# Diccionario para almacenar los usuarios
users = {}

# Ruta principal de la API
@app.route('/', methods=['GET'])
def home():
    # Devuelve un mensaje de bienvenida como cadena de texto
    return jsonify({"message": "Welcome to the user management API!"}), 200

# Ruta para obtener la lista de usuarios
@app.route('/data', methods=['GET'])
def get_data():
    # Devuelve una lista de los nombres de usuarios
    return jsonify(list(users.keys())), 200

# Ruta para agregar un nuevo usuario
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()  # Obtén los datos del cuerpo de la solicitud
    
    # Verifica si los datos son válidos y si tienen el campo 'username'
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data['username']
    
    # Verifica si el nombre de usuario ya existe
    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    
    # Agrega el usuario al diccionario
    users[username] = {
        "username": username,
        "name": data.get('name', ''),
        "age": data.get('age', 0),
        "city": data.get('city', '')
    }
    
    return jsonify({"message": "User added", "user": users[username]}), 201

# Ruta para obtener los detalles de un usuario por su nombre de usuario
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    # Verifica si el usuario existe
    if username in users:
        return jsonify(users[username]), 200
    else:
        return jsonify({"error": "User not found"}), 404

# Ruta para verificar el estado del API
@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "API is running"}), 200

# Corre la aplicación de Flask
if __name__ == '__main__':
    app.run()
