#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def napis(line):
    """Funkcja buduje napis z trzycyfrowych blokow
    >>> napis([9, 2, 11, 606])
    '009 002 011 606'
    >>> napis([42, 68, 676, 12])
    '042 068 676 012'
    """
    line = [str(i).zfill(3) for i in line]
    return " ".join(line)
            

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()
