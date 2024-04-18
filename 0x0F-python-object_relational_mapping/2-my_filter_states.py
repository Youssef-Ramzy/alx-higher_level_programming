#!/usr/bin/python3
""" This script is to list all the states from hbtn_0e_0_usa database """
import MySQLdb
import sys


def main():
    """ main function """
    con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = con.cursor()
    name = sys.argv[4]
    query = "SELECT * FROM states WHERE name LIKE '{}';".format(name)
    cur.execute(query)
    result = cur.fetchall()
    for row in result:
        print(row)
    con.commit()
    cur.close()
    con.close()


if __name__ == "__main__":
    main()
