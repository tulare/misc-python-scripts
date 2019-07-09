# -*- encoding: utf8 -*-

import sys
import os
import argparse
import sqlite3

def parse_args() :
    """ Parse command line arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'dbname',
        #nargs='?',
        help='sqlite database filename'
    )

    args = parser.parse_args()
    return args

def main() :
    args = parse_args()
    print('{}'.format(args), file=sys.stderr)

    if args.dbname is None :
        return

    if not os.path.isfile(args.dbname) :
        return

    conn = sqlite3.connect(args.dbname)

    for line in conn.iterdump() :
        print(line)

    conn.close()

if __name__ == '__main__' :
    main()
