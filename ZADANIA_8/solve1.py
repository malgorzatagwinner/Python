#!usr/bin/env python3
# -*- coding: utf -8-*-
import sys
    
def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0.
    >>> solve1(0,0,0)
    Równanie wskazuje na całą płaszczyznę!
    >>> solve1(0,0,1)
    Równanie sprzeczne!
    >>> solve1(0,0,33)
    Równanie sprzeczne!
    >>> solve1(0,1,0)
    y = 0
    >>> solve1(0,52, 0)
    y = 0
    >>> solve1(1,0,0)
    x = 0
    >>> solve1(52,0,0)
    x = 0
    >>> solve1(1,0,1)
    x = -1.0
    >>> solve1(5,0,1)
    x = -0.2
    >>> solve1(0, 4, 8)
    y = -2.0
    >>> solve1(2, 4, 8)
    y = -0.5x + -2.0
    """    
    if a == 0:
        if b == 0:
            if c== 0:
                print("Równanie wskazuje na całą płaszczyznę!")
                return
            else:
                print("Równanie sprzeczne!")
                return
        else:
            if c==0:
                print("y = 0")
                return
            else:
                print("y = " + str((-c)/b ))    
                return
    elif b == 0:
        if c == 0:
            print("x = 0")
            return
        else:
            print("x = " + str(-c/a ))
            return
    
    a = -a/b
    c = -c/b
    print("y = " + str(a) +"x + " +str(c))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
