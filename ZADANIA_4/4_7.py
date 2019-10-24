#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys
def flatten(sequence):
    """ Funkcja zwraca sume liczb z sekwencji, ktora moze byc zagniezdzona
    >>> flatten([1, [2, [3]]])
    [1, 2, 3]
    >>> flatten([1,(2,3),[],[4,(5,6,7)],8,[9]])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    out = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            out += flatten(item)
        else:
            out.append(item)
    return out

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()

