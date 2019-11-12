#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

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

def fibonacci(n):
    """ Funkcja zwraca n-ty wyraz ciagu Fibonacciego
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(6)
    8
    >>> fibonacci(14)
    377
    """
    previous_n = 1
    current_n = 0
    for i in range(1, n+1):
        current_n += previous_n
        current_n, previous_n = previous_n, current_n
    return current_n

