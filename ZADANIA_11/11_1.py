#!usr/bin/env python3
# -*- coding: utf -8-*-
import random as r
import statistics as s
from random import gauss as g

def ad_a(n):
    lista = list(range(n))
    r.shuffle(lista)
    return lista

def ad_b(n):
    return[n-1] + list(range(n-1))

def ad_c(n):
    return list(range(n-2, -1, -1)) +[n-1]

def ad_d(n, mean=1.0, sigma=1.0):
    while n>0:
        yield g(mean, sigma)
        n-=1

def my_sqrt(n):
    x = n
    y = (x+1) // 2
    while y<x:
        x = y
        y = (x+n // x)//2
    return x

def ad_e(n):
    max = my_sqrt(n)
    while n > 0:
        yield r.randint(0, max)
        n-=1
if __name__ == '__main__':
    print(ad_a(5))
    print(ad_b(5))
    print(ad_c(5))
    print(list(ad_d(5)))
    print(list(ad_e(5)))
