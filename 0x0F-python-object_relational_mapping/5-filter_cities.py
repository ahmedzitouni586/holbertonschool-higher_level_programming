#!/usr/bin/python3
"""
 takes in the name of a state as an argument and lists
 all cities of that state
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
    s = (argv[4], )
    c = "SELECT cities.name FROM cities JOIN states ON\
    cities.state_id = states.id AND states.name = %s ORDER BY cities.id ASC"

    curss.execute(s, c)
    table = curss.fetchall()
    i = [row[0] for row in table]
    together = ", ".join(i)
    print(together)

    curss.close()
    db.close()
if __name__ == "__main__":
    main()
