#!/usr/bin/python3
"""
Script that lists all State objects
containing the letter 'a' from the database
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

    # Filtrar estados que contienen la letra "a" y ordenar por id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Imprimir cada estado que contiene "a" en el nombre
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Cerrar la sesión
    session.close()
