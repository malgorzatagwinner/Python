#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def liczenie(line):
    """ Funkcja znajduje liczbe cyfr zero w liczbie calkowitej
    >>> liczenie(1010101010)
    5
    >>> liczenie(10000000000)
    10
    >>> liczenie(10000000000000000000000000000000000000000)
    40
    """
    return str(line).count('0')

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
                liczenie(f.read())
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        liczenie(data)




