#!usr/bin/env python3
# -*- coding: utf -8-*-
import sys
import cmath
import math
import timeit

def equal(a, b):
    if len(a)>len(b):
        a, b = b, a
    for i in range(len(a)):
        if(a[i] != b[i]):
            return False
    return True

def FFT(a, w):
    if len(a) == 1:
        return a;
    w2 = complex(1,0)
    a_even = a[::2]
    a_odd = a[1::2]

    y1 = FFT(a_even, w*w)
    y2 = FFT(a_odd, w*w)
    
    y = [None] *len(a)

    for i in range (0, len(a)//2 ):
        y[i] = y1[i] + w2 * y2[i]
        y[(len(a)//2)+i] = y1[i] - w2 * y2[i]
        w2 = w*w2
    return y

def count(a, b):
    number = len(a) + len(b)
       
#sprawdzamy najwieksza potege 2, ktora jest wieksza lub rowna sumie dlugosci naszych wielomianow
    number = 2**(number-1).bit_length()
    a += [0]*(number - len(a))
    b += [0]*(number - len(b))

    w = complex(math.cos(2*math.pi/number), math.sin(2*math.pi/number))
    w1 = complex(1.0, 0)/w
    
    A = FFT(a, w)
    B = FFT(b, w)
    
    C = [None]*number
    for i in range(0,number):
        C[i] = (A[i] * B[i])

    tmp = FFT(C, w1)
    c = [None]*number
    for i in range(number):
        c[i] = round((1/number)*tmp[i].real)

    return c
if __name__ == '__main__':
#   elapsed = timeit.timeit(code, number=100)/100
 #  print(elapsed
    from random import seed, randint
#    seed(16)
    a = [randint(-20, 20) for i in range(500)]
    b = [randint(-20, 20) for i in range(500)]
    
    import time
    start_FFT = time.time()
    wynikFFT = count(a,b)
    end_FFT = time.time()
    print("Czas FFT: " + str(end_FFT - start_FFT))
    from poly import Poly
    wynikFFT = Poly(wynikFFT)
    
    start = time.time()
    wynikPoly = Poly(a)*Poly(b)
    end = time.time()
    print("Czas mnożenia: " + str(end - start))
    print(wynikFFT == wynikPoly)
