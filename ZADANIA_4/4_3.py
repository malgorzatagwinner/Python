#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def factorial(n):
    """ Funkcja oblicza silnie podanej w argumencie liczby
    >>> factorial(5)
    120
    >>> factorial(10)
    3628800
    >>> factorial(15)
    1307674368000
    """
    out = 1
    while(n>0):
        out *= n
        n-=1
    return out

if __name__ == '__main__':
    import doctest
    doctest.testmod()
