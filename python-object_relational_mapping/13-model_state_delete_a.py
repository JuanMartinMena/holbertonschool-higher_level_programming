#!/usr/bin/python3
"""
Deletes all State
objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Set up the database connection
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}',
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete states containing 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
