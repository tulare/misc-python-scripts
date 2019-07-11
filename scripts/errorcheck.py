# -*- encoding: utf-8 -*-

import sys
import argparse
import logging

def parse_args() :
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'error',
        nargs='?',
        type=int,
        help='error code'
    )
    args = parser.parse_args()
    return args
    
if __name__ == '__main__' :
    logging.basicConfig(level=logging.DEBUG)

    args = parse_args()
    logging.info(args)
    sys.exit(args.error)
