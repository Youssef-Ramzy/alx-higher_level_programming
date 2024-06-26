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
    name_of_state = sys.argv[4]
    query = """SELECT c.name
                FROM cities AS c
                INNER JOIN states AS s ON c.state_id = s.id
                WHERE s.name = %s
                ORDER BY c.id ASC;
                """
    cur.execute(query, (name_of_state,))
    result = cur.fetchall()
    cities = []
    for row in result:
        cities.append(row[0])
    print(", ".join(cities))
    con.commit()
    cur.close()


if __name__ == "__main__":
    main()
