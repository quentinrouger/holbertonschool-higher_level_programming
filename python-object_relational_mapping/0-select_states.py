#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa."""

import MySQLdb
import sys


conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=mysql_username, passwd=mysql_password, db=database_name
    )
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

if __name__ == "__main__":
    mysql_username, mysql_password, database_name = sys.argv[1],\
        sys.argv[2], sys.argv[3]
    get_all_states(mysql_username, mysql_password, database_name)
