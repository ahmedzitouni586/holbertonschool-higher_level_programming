#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa


if __name__ == '__main__':
    import MySQLdb
    from sys import argv


    username = argv[1];
    password = argv[2];
    dbname = argv[3];


    # open database connection
    db = MySQLdb.connect(
        host ="localhost",
        user =username,
        passwd =password,
        db =dbname,
        port =3306
    )
    # prepare a cursor object using cursor()
    cursor = db.cursor()

    # execute SQL query using execute()
    cursor.execute(
        'SELECT * FROM stats ORDER BY id ASC'
    )

    # fetch rows using fetchall()
    data = cursor.fetchall()
    for row in data:
        print(row)
