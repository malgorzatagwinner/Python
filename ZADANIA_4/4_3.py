#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def number():
    while True:
        linia = input('Podaj liczbe: ')
        try:
            number = int(linia)
        except ValueError:
            print('To nie jest liczba, sprobuj jeszcze raz!')
        else:
            return number


def factorial(n):
    """ Funkcja oblicza silnie podanej w argumencie liczby
    >>> factorial(5)
    120
    >>> factorial(10)
    3628800
    >>> factorial(15)
    1307674368000
    """
    out = 1
    while(n>0):
        out *= n
        n-=1
    return out

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    n = number()
    print('Silnia z liczby ' + str(n) + ' to: ' + str(factorial(n))) 
