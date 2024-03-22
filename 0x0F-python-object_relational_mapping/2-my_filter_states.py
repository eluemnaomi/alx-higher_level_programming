#!/usr/bin/python3

"""
This script takes in an argument and displays all values in the 'states'
table of 'hbtn_0e_0_usa' where 'name' matches the argument
"""

import sys
import MySQLdb

if __name__ == '__main__':

    args = sys.argv

    db = MySQLdb.connect(host='localhost',
                         user=args[1], passwd=args[2], db=args[3])

    conn = db.cursor()

    conn.execute("SELECT * FROM states \
        WHERE CONVERT(`name` using Latin1) \
        COLLATE latin1_General_CS = '{}';".format(args[4]))

    states = conn.fetchall()

    for state in states:
        print(state)
