# -*- encoding: utf-8 -*-

import argparse
import logging
from pathlib import Path
import shutil

# ------------------------------------------------------------------------------

def parse_args() :
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'pattern',
        help='pattern for finding files (ex: **/*.jpg, */*/*.jpg)'
    )
    parser.add_argument(
        '--move',
        action='store_true',
        help='move files, at your own risk'
    )
    parser.add_argument(
        '--copy',
        action='store_true',
        help='copy files, at your own risk'
    )
    parser.add_argument(
        '--into',
        default='',
        help='place files into this folder'
    )   
    parser.add_argument(
        '--clean',
        action='store_true',
        help='clean empty dirs, at your own risk'
    )
    args = parser.parse_args()
    logging.info(args)
    return args

# ------------------------------------------------------------------------------

def recur_clean_empty(path) :

    # recursion
    for rep in (r for r in path.iterdir() if r.is_dir()) :
        logging.debug('inspect -> {}'.format(rep))
        recur_clean_empty(rep)

    # stop condition and postfix clean empty
    if len(list(path.iterdir())) == 0 :
        logging.info('[CLEAR] {}'.format(path))
        path.rmdir()

# ------------------------------------------------------------------------------        

if __name__ == '__main__' :

    # Default logging level
    logging.basicConfig(level=logging.INFO)

    args = parse_args()

    p = Path('.')

    # --into has sense only for move or copy
    if args.move or args.copy :
        if not Path(args.into).is_dir() :
            Path(args.into).mkdir()
    
    for file in [item for item in p.glob(args.pattern) if item.is_file()] :
        new_file = Path(args.into) / Path('_'.join(file.parts))
        if args.move :
            logging.info('[MOVE] {} -> {}'.format(file, new_file))
            file.rename(new_file)
        if args.copy :
            logging.info('[COPY] {} -> {}'.format(file, new_file))
            shutil.copy(file, new_file)

    if args.clean :
        recur_clean_empty(p)
