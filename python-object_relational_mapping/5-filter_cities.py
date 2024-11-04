#!/usr/bin/python3
"""
Este módulo se conecta a una base de datos MySQL y recupera
todas las ciudades de un estado específico de la tabla 'cities'.
"""

import MySQLdb
import sys


def main():
    # Obtener los argumentos de la línea de comandos
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Conectar a la base de datos MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Crear un objeto cursor
    cursor = db.cursor()

    # Consulta SQL para obtener las ciudades del estado especificado
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    
    # Ejecutar la consulta SQL con el estado como parámetro
    cursor.execute(query, (state_name,))

    # Obtener todos los resultados
    results = cursor.fetchall()

    # Extraer los nombres de las ciudades de los resultados
    cities = [row[0] for row in results]

    # Mostrar los resultados como una cadena separada por comas
    print(", ".join(cities))

    # Cerrar el cursor y la conexión
    cursor.close()
    db.close()


# Asegurarse de que el script se ejecute solo
# cuando se ejecuta directamente
if __name__ == "__main__":
    main()
