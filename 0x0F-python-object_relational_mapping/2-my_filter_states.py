#!/usr/bin/python3
"""
 takes in an argument and displays all values in the states table
 where name matches the argument.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    with MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306) as db:
        db.execute("SELECT * FROM states WHERE\
        BINARY name = '{:s}'  ORDER BY states.id".format(argv[4]))
        table = db.fetchall()
        for data in table:
            print(data)
