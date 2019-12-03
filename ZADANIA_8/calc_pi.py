#!usr/bin/env python3
# -*- coding: utf -8-*-
import sys
import math as m
import random as r

def calc_pi(n=100):
    """Obliczanie pi metodą Monte Carlo. n oznacza liczbę losowanych punktów."""
    inside = 0
    for i in range(n):
        dist = m.sqrt(r.random()**2 + r.random()**2)

        if dist<1.0:
            inside+=1
        
    pi = ( float(inside)/n ) * 4

    return pi

if __name__ == '__main__':
    print(calc_pi(75))
    print(calc_pi(1000))
    print(calc_pi(10000))
