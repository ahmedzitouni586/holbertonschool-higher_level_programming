#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    with MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306) as db:
        db.execute("SELECT * FROM states WHERE\
        name LIKE BINARY 'N%' ORDER BY states.id")
        table = db.fetchall()
        for data in table:
            print(data)
