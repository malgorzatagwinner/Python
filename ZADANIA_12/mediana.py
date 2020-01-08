#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def mediana_sort(lista, left, right):
    """ Funkcja zwracajaca mediany listy nieuporzadkowanej
    >>> mediana_sort([3,5,17,2,47,1,50], 0,6)
    5
    >>> mediana_sort([3,5,17,2,47,1,50], 1, 4)
    11.0
    >>> mediana_sort([3,5,17,2,47,1,50], 2, 5)
    9.5
    >>> mediana_sort([3,5,17,2,47,1,50], 2, 6)
    17
    
    """
    lista = lista[left:right+1]
    lista.sort()
    
    if len(lista) %2 == 0:
        mediana1 = lista[len(lista) //2]
        mediana2 = lista[len(lista) //2 -1]
        mediana = (mediana1 + mediana2)/2
    else:
        mediana = lista[len(lista)//2]
    return mediana

if __name__ == '__main__':
    import doctest
    doctest.testmod()
