#!/usr/bin/env python3
# -*- coding: utf-8-*-
import sys

def numberofwords(line):
    """Funkcja zwraca liczbę wyrazow w podanym w argumencie stringu
    >>> numberofwords('test numer jeden')
    3
    >>> numberofwords('To juz jest drugi test')
    5
    >>> numberofwords('Teraz to juz tutaj bedzie siedem slow')
    7
    """
    return len(line.split())

if __name__ == '__main__':
    #testy
    import doctest
    doctest.testmod()

    if len(sys.argv) > 1:
        # w podanych plikach
        for filename in sys.argv[1:]:
            with open(filename) as f:
                print('W tym stringu jest ', numberofwords(f.read()), ' wyrazow')
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        print('W tym stringu jest ', numberofwords(data), ' wyrazow')
