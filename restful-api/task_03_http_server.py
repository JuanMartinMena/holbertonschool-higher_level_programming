from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Manejar la solicitud de acuerdo al endpoint
        if self.path == '/':
            # Respuesta para la ruta raíz
            self.send_response(200)  # Código de estado 200 OK
            self.send_header('Content-type', 'text/plain')  # Tipo de contenido de la respuesta
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')  # Mensaje de respuesta
        elif self.path == '/data':
            # Respuesta para la ruta /data
            self.send_response(200)  # Código de estado 200 OK
            self.send_header('Content-type', 'application/json')  # Tipo de contenido JSON
            self.end_headers()
            # Datos de ejemplo en formato JSON
            simple_data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(simple_data).encode())  # Convertir a JSON y enviar
        elif self.path == '/status':
            # Respuesta para la ruta /status
            self.send_response(200)  # Código de estado 200 OK
            self.send_header('Content-type', 'text/plain')  # Tipo de contenido de la respuesta
            self.end_headers()
            self.wfile.write(b'OK')  # Mensaje de respuesta
        else:
            # Manejar rutas no definidas
            self.send_response(404)  # Código de estado 404 Not Found
            self.send_header('Content-type', 'text/plain')  # Tipo de contenido de la respuesta
            self.end_headers()
            self.wfile.write(b'Endpoint not found')  # Mensaje de error

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ('', port)  # Escuchar en todas las interfaces de red en el puerto especificado
    httpd = server_class(server_address, handler_class)  # Crear el servidor
    print(f'Starting server on port {port}...')
    httpd.serve_forever()  # Iniciar el servidor

if __name__ == "__main__":
    run()  # Ejecutar el servidor
