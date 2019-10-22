#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def zmiana(line):
    """ Funkcja sortuje wyrazy z podanego stringa raz alfabetycznie, a raz pod wzgledem dlugosci
    >>> zmiana('Kasia Asia')
    ['Asia', 'Kasia']
    >>> zmiana('stary tekst')
    ['stary', 'tekst']
    >>> zmiana('piesek zolw kotek')
    ['kotek', 'piesek', 'zolw']
    """

    line = line.split()
    line.sort()
    return line   
    
def zmianadlugosc(line):
    """ Funkcja sortuje wyrazy z podanego stringa raz alfabetycznie, a raz pod wzgledem dlugosci
    >>> zmianadlugosc('Kasia Asia')
    ['Asia', 'Kasia']
    >>> zmianadlugosc('tekst tekstowy')
    ['tekst', 'tekstowy']
    >>> zmiana('piesek zolw kotek')
    ['kotek', 'piesek', 'zolw']
    """
    line = line.split()
    line.sort(key = len)
    return line

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()

    if len(sys.argv) > 1:
        # w podanych plikach
        for filename in sys.argv[1:]:
            if filename.startswith('-'):
                continue
            with open(filename) as f:
                zmiana(f.read())
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        zmiana(data)

