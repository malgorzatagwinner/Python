#!usr/bin/env python3
# -*- coding: utf -8-*-
import sys
import math as m

def isfloat(a):
        try:
            a = float(a)
            return True
        except (TypeError, ValueError):
            return False

            
def heron(a, b, c):
    """ Obliczanie pola powierzchni trójkąta za pomocą wzoru Herona. Długości boków trójkąt wynoszą a, b, c.
    >>> heron(3, 4 ,5)
    6.0
    >>> heron(1, 2, 3)
    0.0
    >>> '{:.3f}'.format(heron(2, 3, 4))
    '2.905'
    >>> heron(3, 4, 8)
    Traceback (most recent call last):
        ...
    ValueError: Z tych boków nie można zrobić trójkąta!
    >>> heron('test', 4, 8)
    Traceback (most recent call last):
        ...
    ValueError: 'test' nie jest liczbą
    >>> heron(4, 'test', 8)
    Traceback (most recent call last):
        ...
    ValueError: 'test' nie jest liczbą
    >>> heron(4, 8, 'test')
    Traceback (most recent call last):
        ...
    ValueError: 'test' nie jest liczbą
    """
    if not isfloat(a):
        raise ValueError(f"'{a}' nie jest liczbą")
    a=float(a)

    if not isfloat(b):
        raise ValueError(f"'{b}' nie jest liczbą")
    b=float(b)
    if not isfloat(c):
        raise ValueError(f"'{c}' nie jest liczbą")
    c = float(c)

    if not(a + b < c or a + c < b or b + c < a):
        p = 1/2 *(a+b+c)
        S = m.sqrt(p*(p-a)*(p-b)*(p-c))
        return S
    else:
        raise ValueError("Z tych boków nie można zrobić trójkąta!")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
