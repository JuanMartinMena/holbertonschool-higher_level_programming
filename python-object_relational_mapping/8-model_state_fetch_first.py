#!/usr/bin/python3
"""
Script that prints the first State
object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Crear la conexión con la base de datos
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', 
        pool_pre_ping=True
    )
    # Crear una sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Obtener el primer State ordenado por id
    first_state = session.query(State).order_by(State.id).first()

    # Imprimir el resultado o "Nothing" si no hay resultados
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Cerrar la sesión
    session.close()
