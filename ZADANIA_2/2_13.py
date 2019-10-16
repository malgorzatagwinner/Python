#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def sumaliter(line):
    line = line.split()
    out = 0
    for i in line:
        out+=len(i)
    print(out)

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
                sumaliter(f.read())
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        sumaliter(data)
