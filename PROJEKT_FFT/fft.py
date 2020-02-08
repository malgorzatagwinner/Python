#!usr/bin/env python3
# -*- coding: utf -8-*-
import sys
import cmath
import math
import timeit
import numpy as np

def FFT(a, w):
    if len(a) == 1:
        return a;
    w2 = complex(1,0)
    a_even = a[::2]
    a_odd = a[1::2]

    y1 = FFT(a_even, w*w)
    y2 = FFT(a_odd, w*w)
    
    y = np.zeros(len(a), dtype = complex)

    for i in range (0, len(a)//2 ):
        y[i] = y1[i] + w2 * y2[i]
        y[(len(a)//2)+i] = y1[i] - w2 * y2[i]
        w2 = w*w2
    return y

def count(a, b):
    number = len(a) + len(b)
       
#sprawdzamy najwieksza potege 2, ktora jest wieksza lub rowna sumie dlugosci naszych wielomianow
    number = 2**(number-1).bit_length()
    tmp = np.zeros((number - len(a)))
    a = np.concatenate((a, tmp), axis = 0)
    tmp = np.zeros((number - len(b)))
    b = np.concatenate((b, tmp), axis = 0)
    #a += [0]*(number - len(a))
    #b += [0]*(number - len(b))

    w = complex(math.cos(2*math.pi/number), math.sin(2*math.pi/number))
    w1 = complex(1.0, 0)/w
    
    A = FFT(a, w)
    B = FFT(b, w)
    
    C = A * B

    tmp = FFT(C, w1)
    c = np.zeros(number)
    for i in range(number):
        c[i] = round((1/number)*tmp[i].real)

    return c
