#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Crear la conexión a la base de datos usando los argumentos proporcionados
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)

    # Crear una sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Consultar todos los objetos State, ordenados por id
    states = session.query(State).order_by(State.id).all()

    # Imprimir los resultados
    for state in states:
        print(f"{state.id}: {state.name}")

    # Cerrar la sesión
    session.close()
