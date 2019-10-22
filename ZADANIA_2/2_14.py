#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def najdluzszy(line):
    """ Funkcja znajduje najdluzszy wyraz w podanym stringu oraz jego dlugosc
    >>> najdluzszy('Tu ja jestem najdluzszy')
    ('najdluzszy', 10)
    >>> najdluzszy('Superkalifradalistodekspialitycznie fajnie')
    ('Superkalifradalistodekspialitycznie', 35)
    """
    line = line.split()
    out = ''
    out_len = 0;
    for i in line:
        if out_len < len(i):
            out_len = len(i)
            out = i

    return(out, out_len)

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
                (length, word) = najdluzszy(f.read())
                print(f'{filename}: Najdluzsze slowo: "{out}" (dlugosc: {length})')
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        (length, word) = najdluzszy(data)
        print(f'Najdluzsze slowo: {word} (dlugosc: {length})')
