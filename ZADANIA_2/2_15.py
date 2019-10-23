#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def ciag(numbers):
    """ Funkcja tworzy napis bedacy ciagiem cyfr kolejnych liczb z podanej listy
    >>> ciag([3, 2, 1, 7])
    '3217'
    >>> ciag([33, 3, 444, 55, 5])
    '333444555'
    """
    wynik = ''
    for i in numbers:
        wynik+=str(i)
    return wynik

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()
    
    if len(sys.argv)>1:
        #w podanych plikach
        for filename in sys.argv[1:]:
            if filename.startswith('-'):
                continue
            with open(filename) as f:
                print(f'{filename}: {ciag()}')
    else:
    # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        data = map(int, data.split())
        print(ciag(data))

