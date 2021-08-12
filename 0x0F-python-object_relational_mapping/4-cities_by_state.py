#!/usr/bin/python3
"""
 takes in an argument and displays all values in the states table
"""


def main():
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    curss = db.cursor()
    curss.execute("SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id")
    table = curss.fetchall()
    for row in table:
        print(row)
    curss.close()
    db.close()
if __name__ == "__main__":
    main()
