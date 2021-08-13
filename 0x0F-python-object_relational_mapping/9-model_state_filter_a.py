#!/usr/bin/python3
"""
lists States objects that contins "a" from the database hbtn_0e_6_usa
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
import model_state
from model_state import Base, State
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    rows = session.query(State).filter(
                              State.name.like('%a%')).order_by(State.id)
    for i in rows:
        print("{}: {}".format(i.id, i.name))
    session.close()
