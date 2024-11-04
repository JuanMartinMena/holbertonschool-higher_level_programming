#!/usr/bin/python3
"""
Este módulo se conecta a una base de datos MySQL y recupera
todos los estados de la tabla 'states' cuyo nombre comienza
con la letra 'N'.
"""


import MySQLdb
import sys


def main():
    # Obtener los argumentos de la línea de comandos
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Ejecutar la consulta SQL para seleccionar estados que comienzan con 'N'
    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")

    # Obtener todos los resultados
    results = cursor.fetchall()

    # Mostrar los resultados
    for row in results:
        print(row)

    # Cerrar el cursor y la conexión
    cursor.close()
    db.close()


# Asegurarse de que el script se ejecute solo cuando se ejecuta directamente
if __name__ == "__main__":
    main()
