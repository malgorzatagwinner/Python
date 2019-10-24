#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys
def sum_seq(sequence):
    """ Funkcja zwraca sume liczb z sekwencji, ktora moze byc zagniezdzona
    >>> sum_seq([1])
    1
    >>> sum_seq([])
    0
    >>> sum_seq([1, [2, [3]]])
    6
    >>> sum_seq((1, 2))
    3
    >>> sum_seq([1,(2,3),[],[4,(5,6,7)],8,[9]])
    45
    """
    out = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            out += sum_seq(item)
        else:
            out += item
    return out

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()
