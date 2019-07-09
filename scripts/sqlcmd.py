# -*- encoding: utf8 -*-
# A minimal SQLite shell for experiments

import os
import sys
import argparse
import sqlite3

# ------------------------------------------------------------------------------

def database_connect(dbname, create=False) :
    conn = None

    if dbname is None :
        return

    if not os.path.isfile(dbname) and not create :
        print("Error: '{}' is not a database".format(dbname), file=sys.stderr)
        return

    try :
        conn = sqlite3.connect(dbname)
        conn.execute('select * from sqlite_master')
    except Exception as e :
        print("Error: '{}' {}".format(dbname, repr(e)), file=sys.stderr)
        if conn is not None :
            conn.close()
        return

    return conn

# ------------------------------------------------------------------------------    

def parse_args() :
    """ Parse command line arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-c', '--create',
        action='store_true',
        help='create dabatase if not exists'
    )

    parser.add_argument(
        'dbname',
        #nargs='?',
        help='sqlite database filename'
    )
    
    args = parser.parse_args()
    return args

# ------------------------------------------------------------------------------

def main() :

    args = parse_args()
    print('{}'.format(args), file=sys.stderr)


    conn = database_connect(args.dbname, args.create)
    if conn is None :
        return
    
    conn.isolation_level = None
    cur = conn.cursor()

    buffer = ""

    print("Enter your SQL commands to execute in sqlite3.")
    print("Enter .quit to exit.")

    while True :
        line = input()
        if line == ".quit":
            break
        buffer += line
        if sqlite3.complete_statement(buffer):
            try :
                buffer = buffer.strip()
                cur.execute(buffer)

                if buffer.lstrip().upper().startswith("SELECT") :
                    print(cur.fetchall())

                if buffer.lstrip().upper().startswith("PRAGMA") :
                    print(cur.fetchall())

            except sqlite3.Error as e :
                print(repr(e))
            buffer = ""

    conn.close()

# ------------------------------------------------------------------------------

if __name__ == '__main__' :
    main()
