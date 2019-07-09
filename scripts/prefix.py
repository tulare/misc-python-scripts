# -*- encoding: utf-8 -*-

import argparse
from pathlib import Path


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
        '-H', '--remove-head',
        default=''
    )
    parser.add_argument(
        '-T', '--remove-tail',
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
        '-C', '--mod-from',
        default=''
    )
    parser.add_argument(
        '-E', '--to-end',
        default=''
    )    
    parser.add_argument(
        '-Y', '--by',
        default=''
    )
    args = parser.parse_args()
    print(args)
    return args

def add_before(file, text='') :
    new_name = text + file.name
    file.rename(new_name)
    print(new_name)

def add_after(file, text='') :
    new_name = file.stem + text + file.suffix
    file.rename(new_name)
    print(new_name)

def remove_tail(file, here='') :
    new_name = file.name
    parts = file.stem.rpartition(here)
    if parts[1] == here and parts[2] == '' :
        new_name = parts[0] + file.suffix
        file.rename(new_name)
    print(new_name)

def remove_head(file, here='') :
    new_name = file.name
    parts = file.stem.partition(here)
    if parts[1] == here and parts[0] == '' :
        new_name = parts[2] + file.suffix
        file.rename(new_name)
    print(new_name)

def cut_before(file, here='') :
    new_name = file.name
    parts = file.stem.partition(here)
    if parts[1] == here and parts[0] != '' :
        new_name = parts[2] + file.suffix
        file.rename(new_name)
    print(new_name)

def cut_after(file, here='') :
    new_name = file.name
    parts = file.stem.partition(here)
    if parts[1] == here and parts[2] != '' :
        new_name = parts[0] + file.suffix
        file.rename(new_name)
    print(new_name)

def mod_left(file, here='', by='') :
    new_name = file.name
    parts = file.stem.partition(here)
    if parts[1] == here :
        new_name = parts[0] + by + parts[2] + file.suffix
        file.rename(new_name)
    print(new_name)

def mod_right(file, here='', by='') :
    new_name = file.name
    parts = file.stem.rpartition(here)
    if parts[1] == here :
        new_name = parts[0] + by + parts[2] + file.suffix
        file.rename(new_name)
    print(new_name)

def mod_center(file, start='', end='', by='') :
    new_name = file.name
    sparts = file.stem.partition(start)
    if sparts[1] == start :
        eparts = sparts[2].partition(end)
        if eparts[1] == end :
            new_name = sparts[0] + by + eparts[2] + file.suffix
            file.rename(new_name)
    print(new_name)
        

if __name__ == '__main__' :

    args = parse_args()

    p = Path('.')
    for file in (x for x in p.glob(args.pattern) if x.is_file()) :
        print(file, end=' -> ')
        if args.add_before != '' :
            add_before(file, args.add_before)
        if args.add_after != '' :
            add_after(file, args.add_after)
        if args.remove_head != '' :
            remove_head(file, args.remove_head)
        if args.remove_tail != '' :
            remove_tail(file, args.remove_tail)
        if args.cut_before != '' :
            cut_before(file, args.cut_before)
        if args.cut_after != '' :
            cut_after(file, args.cut_after)
        if args.mod_left != '' :
            mod_left(file, args.mod_left, args.by)
        if args.mod_right != '' :
            mod_right(file, args.mod_right, args.by)
        if args.mod_from != '' and args.to_end != '' :
            mod_center(file, start=args.mod_from, end=args.to_end, by=args.by)
        
