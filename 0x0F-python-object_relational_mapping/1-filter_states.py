#!/usr/bin/python
"""
Lists states start with N from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    # connect
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # cursor
    cursor = db.cursor()

    # execute query
    cursor.execute("SELECT * FROM states WHERE\
    name LIKE BINARY 'N%' ORDER BY states.id")

    # fetch and print
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # close cursor and database
    cursor.close()
    db.close()
