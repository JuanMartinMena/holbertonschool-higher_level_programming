import requests
import csv

# Función para obtener los posts y mostrar sus títulos
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Imprime el código de estado de la respuesta
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        # Convierte la respuesta en JSON
        posts = response.json()

        # Itera sobre los posts y muestra los títulos
        for post in posts:
            print(post['title'])
    else:
        print("Error al obtener los datos.")

# Función para obtener los posts y guardarlos en un archivo CSV
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        # Convierte la respuesta en JSON
        posts = response.json()

        # Crea una lista de diccionarios con id, title y body
        data_to_save = [{"id": post['id'], "title": post['title'], "body": post['body']} for post in posts]

        # Guarda los datos en un archivo CSV
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data_to_save)

        print("Datos guardados en posts.csv")
    else:
        print("Error al obtener los datos.")
