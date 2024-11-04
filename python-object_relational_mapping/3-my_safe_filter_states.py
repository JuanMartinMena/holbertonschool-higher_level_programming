#!/usr/bin/python3
"""
Este módulo se conecta a una base de datos MySQL y recupera
todos los estados de la tabla 'states' que coinciden con el
nombre del estado proporcionado como argumento, de manera segura
contra inyecciones SQL.
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

    # Crear la consulta SQL utilizando un placeholder
    query = (
        "SELECT * FROM states "
        "WHERE name = %s "
        "ORDER BY id ASC"
    )

    # Ejecutar la consulta SQL de manera segura con un placeholder
    cursor.execute(query, (state_name,))

    # Obtener todos los resultados
    results = cursor.fetchall()

    # Mostrar los resultados
    for row in results:
        print(row)

    # Cerrar el cursor y la conexión
    cursor.close()
    db.close()


# Asegurarse de que el script se ejecute solo
# cuando se ejecuta directamente
if __name__ == "__main__":
    main()
