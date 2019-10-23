#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys, random

roman_val = { 'I': 1, 'V' : 5, 'X' : 10, 'L': 50, 'C': 100, 'D' : 500, 'M' : 1000 }
def roman2int(line):
    """ Funkcja zmienia liczby rzymskie na arabskie
    >>> roman2int('I')
    1
    >>> roman2int('II')
    2
    >>> roman2int('XL')
    40
    >>> roman2int('MCMLXXXVII')
    1987
    >>> roman2int('MMMCMLXXXVI')
    3986
    >>> roman2int('MMMM')
    4000
    >>> roman2int('DCLXVI')
    666
    """
    line = line.strip()
    out = 0
    for i in range(len(line)):
        if(i+1!= len(line) and roman_val[line[i]] < roman_val[line[i+1]]):
            out -= roman_val[line[i]]
        else:
            out+= roman_val[line[i]]
    

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
                print(roman2int(f.read()))
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        print(roman2int(data))

    
