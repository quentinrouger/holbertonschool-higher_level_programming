#!/usr/bin/python3
"""
script that prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    q = session.query(City, State).join(State).all()
    for city, state in q:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
