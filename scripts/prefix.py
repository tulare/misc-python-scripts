# -*- encoding: utf-8 -*-

import argparse
import logging
from pathlib import Path

# ------------------------------------------------------------------------------

def parse_args() :
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'pattern'
    )
    parser.add_argument(
        '-F', '--add-before',
        default=''
    )
    parser.add_argument(
        '-Z', '--add-after',
        default=''
    )
    parser.add_argument(
        '-B', '--cut-before',
        default=''
    )
    parser.add_argument(
        '-A', '--cut-after',
        default=''
    )
    parser.add_argument(
        '-L', '--mod-left',
        default=''
    )
    parser.add_argument(
        '-R', '--mod-right',
        default=''
    )
    parser.add_argument(
        '--mod-from',
        default=''
    )
    parser.add_argument(
        '--to',
        default=''
    )    
    parser.add_argument(
        '--by',
        default=''
    )
    args = parser.parse_args()
    logging.debug(args)
    return args

# ------------------------------------------------------------------------------

def add_before(file, text='') :
    new_name = text + file.name
    file.rename(new_name)
    return new_name

# ------------------------------------------------------------------------------

def add_after(file, text='') :
    new_name = file.stem + text + file.suffix
    file.rename(new_name)
    return new_name

# ------------------------------------------------------------------------------

def cut_before(file, here='') :
    new_name = file.name
    parts = file.stem.partition(here)
    if parts[1] == here :
        new_name = parts[2] + file.suffix
        file.rename(new_name)
    return new_name

# ------------------------------------------------------------------------------

def cut_after(file, here='') :
    new_name = file.name
    parts = file.stem.rpartition(here)
    if parts[1] == here :
        new_name = parts[0] + file.suffix
        file.rename(new_name)
    return new_name

# ------------------------------------------------------------------------------

def mod_left(file, here='', by='') :
    new_name = file.name
    parts = file.stem.partition(here)
    if parts[1] == here :
        new_name = parts[0] + by + parts[2] + file.suffix
        file.rename(new_name)
    return new_name

# ------------------------------------------------------------------------------

def mod_right(file, here='', by='') :
    new_name = file.name
    parts = file.stem.rpartition(here)
    if parts[1] == here :
        new_name = parts[0] + by + parts[2] + file.suffix
        file.rename(new_name)
    return new_name

# ------------------------------------------------------------------------------

def mod_center(file, start='', end='', by='') :
    new_name = file.name
    sparts = file.stem.partition(start)
    if sparts[1] == start :
        eparts = sparts[2].rpartition(end)
        if eparts[1] == end :
            new_name = sparts[0] + by + eparts[2] + file.suffix
            file.rename(new_name)
    return new_name

# ------------------------------------------------------------------------------

if __name__ == '__main__' :

    logging.basicConfig(level=logging.INFO)

    args = parse_args()

    p = Path('.')
    for file in (x for x in p.glob(args.pattern) if x.is_file()) :
        new_name = ''
        if args.add_before != '' :
            new_name = add_before(file, args.add_before)
        if args.add_after != '' :
            new_name = add_after(file, args.add_after)
        if args.cut_before != '' :
            new_name = cut_before(file, args.cut_before)
        if args.cut_after != '' :
            new_name = cut_after(file, args.cut_after)
        if args.mod_left != '' :
            new_name = mod_left(file, args.mod_left, args.by)
        if args.mod_right != '' :
            new_name = mod_right(file, args.mod_right, args.by)
        if args.mod_from != '' and args.to != '' :
            new_name = mod_center(file, start=args.mod_from, end=args.to, by=args.by)
        operation = 'FOUND' if new_name == '' else 'RENAME'
        logging.info('[{}] {} {}'.format(operation, file, new_name))
        
