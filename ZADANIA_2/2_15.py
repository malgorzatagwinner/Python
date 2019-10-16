#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def ciag(numbers):
    out = ''
    for i in numbers:
        out+=str(i)
    print(out)

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()
    # na standardowym wejściu
    data = sys.stdin.read().rstrip()
    data = map(int, data.split())
    ciag(data)

