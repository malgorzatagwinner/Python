#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def napis(line):
    line = line.split()
    line = [i.zfill(3) for i in line]
    " ".join(line)
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
                napis(f.read())
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        napis(data)
