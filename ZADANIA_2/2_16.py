#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def zmiana(line):
    """ Funkcja zmienia ciag znakow 'GvR' na 'Guido van Rossum'
    >>> zmiana('GvR wielkim poeta nie byl')
    'Guido van Rossum wielkim poeta nie byl'
    >>> zmiana('GvR III byl najlepszym GvR ze wszystkich GvR')
    'Guido van Rossum III byl najlepszym Guido van Rossum ze wszystkich Guido van Rossum'
    >>> zmiana('GrR GvR Gvr gvr gVr')
    'GrR Guido van Rossum Gvr gvr gVr'
    
    """
    line = line.replace('GvR', 'Guido van Rossum')
    return line

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()

    if len(sys.argv) > 1:
        # w podanych plikach
        for filename in sys.argv[1:]:
            if filename.startswith('-'):
                continue
            with open(filename) as f:
                print(zmiana(f.read()))
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        print(zmiana(data))
