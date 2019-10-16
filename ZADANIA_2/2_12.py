#!/usr/bin/env python3
# -*- coding: utf-8-*-
import sys

def firstchars(words):
    words = words.split()
    out = ''
    for char in words:
        first_char = char[0]
        out += first_char    
    print(out)

def lastchars(words):
    words = words.split()
    out = ''
    for char in words:
        last_char = char[len(char)-1]
        out += last_char
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
                firstchars(f.read())
                lastchars(f.read())
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        firstchars(data)
        lastchars(data)
