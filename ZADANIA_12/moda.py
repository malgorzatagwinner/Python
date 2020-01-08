#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys
import collections as c

def moda(lista, left, right):
    """ Funkcja znajdujaca mode w podanej liscie nieuporzadkowanej
    >>> moda([3,5,17,3,47,1,30], 0, 7);
    [3]
    >>> moda([3,5,17,3,47,1,30,1], 0, 8);
    [3, 1]
    >>> moda([3,5,17,30,47,1,30,1], 0, 8);
    [30, 1]
    >>> moda([3,5,17,3,5,1,30,99,8,9,18,3], 0, 11);
    [3]
    """
    lista = lista[left:right+1]
    data = c.Counter(lista)
    data_dict = dict(data)
    max_value = max(list(data.values()))
    
    moda = [val for val, freq in data_dict.items() if freq == max_value]

    if len(moda) == len(lista):
        print("Brak mody!")
        return
    else:
        return moda
if __name__ == '__main__':
    import doctest
    doctest.testmod()

