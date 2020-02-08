#!usr/bin/env python3
# -*- coding: utf -8-*-
import sys
import cmath
import math
import timeit
import time
from numpy_fft import count2
from fft import count
from fft import FFT
import numpy as np

if __name__ == '__main__':
    from random import seed, randint
    N = 5000
    a = np.array([randint(-20, 20) for i in range(N)])
    b = np.array([randint(-20, 20) for i in range(N)])
    print(f'Rozmiar: {N}')
    

    start_FFT = time.time()
    wynikFFT = count(a,b)
    end_FFT = time.time()
    print("Czas FFT: " + str(end_FFT - start_FFT))
    from poly import Poly
    # wynikFFT = Poly(wynikFFT)
    
    start = time.time()
    wynikPoly = Poly(a.tolist())*Poly(b.tolist())
    end = time.time()
    print("Czas mnożenia: " + str(end - start))

    if Poly(wynikFFT.tolist()) == wynikPoly:
        print('Wynik ok')

    start = time.time()
    wynikNp = count2(a,b)
    end = time.time()
    print("Czas numpy: " + str(end - start))

    # usuń zera z końca
    wynikFFT = np.trim_zeros(wynikFFT, 'b')
    # błędy numeryczne!
    if np.allclose(wynikFFT, wynikNp):
        print('Wynik ok')
