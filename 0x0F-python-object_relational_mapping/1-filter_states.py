#!/usr/bin/python3
'''
Lists all states that start with N from the database hbtn_0e_0_usa
'''

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                        user=argv[1],
                        passwd=argv[2],
                        db=argv[3],
                        port=3306)
    curss = db.cursor()
    curss.execute("SELECT * FROM states WHERE\
    name LIKE BINARY 'N%' ORDER BY states.id")
    table = curss.fetchall()
    for row in table:
        print(row)
    curss.close()
    db.close()
