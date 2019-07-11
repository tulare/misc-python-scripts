# -*- encoding: utf-8 -*-
from __future__ import (
    absolute_import,
    print_function, division,
    unicode_literals
)

from platform import python_version
import os
import sys
import argparse

# -----------------------------------------------------------

def createDesktopIni(path, data) :
    pathname = path + '\\desktop.ini'

    if os.path.isfile(pathname) :
        os.system('attrib -S -H {}'.format(pathname))

    with open(pathname, 'w') as fd :
        fd.write(data)

    os.system('attrib +S +H {}'.format(pathname))

    print('{} : OK'.format(pathname))
    
# --------------------------------------------------------------------

def parse_args() :
    """ Parse command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'root',
        nargs='?',
        default='.'
    )
    parser.add_argument(
        '--purge',
        action='store_true'
    )
    parser.add_argument(
        '--copy',
    )
    args = parser.parse_args()

    return args

# --------------------------------------------------------------------

def main() :
    # Parse command line arguments
    args = parse_args()

    print('Python {}'.format(python_version()), file=sys.stderr)
    print('Arguments : {}'.format(args), file=sys.stderr)

    # fichier modèle
    if args.copy :
        with open(args.copy, 'r') as fd :
            data = fd.read()

    # affichage / purge 
    for root, dirs, files in os.walk(args.root) :
        for file in files :
            pathname = root + '\\' + file
            if 'desktop.ini' in file :
                print(pathname)
                if args.purge :
                    os.remove(pathname)
                
    # copie / diffusion
    if args.copy :
        for root, dirs, files in os.walk(args.root) :
            createDesktopIni(root, data)
        
# --------------------------------------------------------------------

if __name__ == '__main__' :
    main()
