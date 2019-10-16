#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def zmiana(line):
    line = line.split()
    line.sort()
    
    print(line)
    line.sort(key = len)
    print(line)

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

