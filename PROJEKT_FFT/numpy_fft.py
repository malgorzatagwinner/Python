#!usr/bin/env python3
# -*- coding: utf -8-*-
import sys
import numpy as np

def count2(a, b):
    L = len(a) + len(b) - 1

    a_f = np.fft.fft(a, L)
    b_f = np.fft.fft(b, L)

    return np.real(np.fft.ifft(np.multiply(a_f, b_f)))

