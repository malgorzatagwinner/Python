#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def suma_sum(line):
    """ Funkcja zwraca liste zawierajaca sumy liczb z podanych sekwencji
    >>> suma_sum([[],[4], (1,2), [3, 4], (5, 6, 7)])
    [0, 4, 3, 7, 18]
    """
    return list(map(sum,line))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    if len(sys.argv) > 1:
        # w podanych plikach
        for filename in sys.argv[1:]:
            with open(filename) as f:
                print(suma_sum(f.read()))
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        print(suma_sum(data))

