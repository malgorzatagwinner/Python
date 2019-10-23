#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def suma_sum(line):
    """ Funkcja zwraca liste zawierajaca sumy liczb z podanych sekwencji
    >>> suma_sum([[],[4], (1,2), [3, 4], (5, 6, 7)])
    [0, 4, 3, 7, 18]
    >>> suma_sum([[3]])
    [3]
    >>> suma_sum([(1,5), [6, 3], [3,5,7,5,2,3,4,6]])
    [6, 9, 35]
    """
    return list(map(sum,line))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    data = [[], (1,2), [3,4], (5,6,7)]
    print(suma_sum(data))

