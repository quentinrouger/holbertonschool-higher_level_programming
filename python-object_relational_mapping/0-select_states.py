#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def get_all_states(mysql_username, mysql_password, database_name):
    """
    Retrieves and prints all the states from the 'states' table in the given
    MySQL database.

    Parameters:
        mysql_username (str): The MySQL database username.
        mysql_password (str): The MySQL database password.
        database_name (str): The name of the MySQL database.

    Returns:
        None
    """

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=mysql_username, passwd=mysql_password, db=database_name
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()

if __name__ == "__main__":
     mysql_username, mysql_password, database_name = sys.argv[1],\
        sys.argv[2], sys.argv[3]
     get_all_states(mysql_username, mysql_password, database_name)
