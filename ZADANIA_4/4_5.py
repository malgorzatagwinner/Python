#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def reverse_iterative(sequence, left, right):
    """ Funkcja iteratywnie odwraca sekwencję sequence od liczby o indeksie left do right wlacznie
    >>> reverse_iterative([1,2,3,4,5,6], 1, 4)
    [1, 5, 4, 3, 2, 6]
    >>> reverse_iterative([10,9,8,7,6,5,4,3,2,1], 0, 6)
    [4, 5, 6, 7, 8, 9, 10, 3, 2, 1]
    """
    return(sequence[:left] + sequence[left: right+1][::-1] + sequence[right+1:])

def reverse_recursive(sequence, left, right):
    """ Funkcja rekursywnie odwraca sekwencję sequence od liczby o indeksie left fo right wlacznie
    >>> reverse_recursive([1,2,3,4,5,6], 1, 4)
    [1, 5, 4, 3, 2, 6]
    >>> reverse_recursive([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 6)
    [4, 5, 6, 7, 8, 9, 10, 3, 2, 1]
    """
    if right <= left:
        return sequence
    sequence[left], sequence[right] = sequence[right], sequence[left]
    return reverse_recursive(sequence, left+1, right-1)
   
if __name__ == '__main__':
    # testy jednak inaczej
    import doctest
    doctest.testmod()
