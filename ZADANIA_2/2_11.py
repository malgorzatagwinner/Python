#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def kreskowanie(word):
    """Funkcja oddziela slowa podkreslnikiem
    >>> kreskowanie('test jeden')
    'test_jeden'
    >>> kreskowanie('to jest drugi test')
    'to_jest_drugi_test'
    >>> kreskowanie('trzeci test tez nie jest taki trudny')
    'trzeci_test_tez_nie_jest_taki_trudny'
    """
    
    word = "_".join(list(word))
    return word

if __name__ == '__main__':
    #testy
    import doctest
    doctest.testmod()

    if len(sys.argv) > 1:
        # w podanych plikach
        for filename in sys.argv[1:]:
            with open(filename) as f:
                print(kreskowanie(f.read()))
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        print(kreskowanie(data))
  
