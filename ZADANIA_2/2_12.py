#!/usr/bin/env python3
# -*- coding: utf-8-*-
import sys

def firstchars(words):
    """ Funkcja zwraca slowo stworzone z pierwszych liter slow z podanego stringa
    >>> firstchars('Test')
    'T'
    >>> firstchars('Test numer dwa')
    'Tnd'

    """
    words = words.split()
    out = ''
    for char in words:
        first_char = char[0]
        out += first_char    
    return out

def lastchars(words):
    """ Funkcja zwraca slowo stworzone z ostatnich liter slow z podanego stringa
    >>> lastchars('Test')
    't'
    >>> lastchars('Test numer dwa')
    'tra'
    """
    words = words.split()
    out = ''
    for char in words:
        last_char = char[len(char)-1]
        out += last_char
    return out

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
                print(firstchars(f.read()))
                print(lastchars(f.read()))
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        print(firstchars(data))
        print(lastchars(data))
