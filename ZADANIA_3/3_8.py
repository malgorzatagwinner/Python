#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys, random

def common(a, b):
    """Funkcja zwracajaca czesc wspolna dwoch zbiorow
    >>> common([1,2,3,5], [5,4,6,3,8,11])
    [3, 5]
    
    >>> common([3, 11, 21, 2, 1, 7], [11, 37, 12, 21, 17])
    [11, 21]
    """
    return list(set(a) & set(b))
    
def everything(a,b):
    """ Funkcja zwracajaca sume dwoch zbiorow
    >>> everything([3, 4, 5, 6, 7, 8], [5, 12, 14, 7, 8, 9])
    [3, 4, 5, 6, 7, 8, 9, 12, 14]
    """

    return list(set(a+b))

def random_list():
    return [random.randint(0, 10) for _ in range(random.randint(1, 10))]

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    a = random_list()
    b = random_list()
    print(a)
    print(b)
    print()
    print(common(a, b))
    print(everything(a, b))
