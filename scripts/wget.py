# -*- encoding: utf-8 -*-
import os, sys
import shutil
import argparse
import logging
import urllib.request

def parse_args() :
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'url',
        help='url to file to HTTP GET'
    )
    args = parser.parse_args()
    return args

def httpget(url) :
    filename = "./" + os.path.basename(args.url)
    if os.path.exists(filename) :
        logging.error('{} exists'.format(filename))
        return "DESTINATION FILE EXISTS"
    tmpfile, headers = urllib.request.urlretrieve(args.url)
    logging.info(tmpfile)
    shutil.move(tmpfile, filename)
    
if __name__ == '__main__' :
    logging.basicConfig(level=logging.DEBUG)

    args = parse_args()
    logging.info(args)

    sys.exit(httpget(args.url))

