#!/usr/bin/python3
"""
lists States objects that contins 'a' from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def list_all():
    """ list the states """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3])
                           )
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for data in states:
        if 'a' in data.name.lower():
            print("{}: {}".format(data.id, data.name))

if __name__ == '__main__':
    list_all()
