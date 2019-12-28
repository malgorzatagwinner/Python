#!usr/bin/env python3
# -*- coding: utf -8-*-
import random as r
import statistics as s
from random import gauss as g

def lista(n):
    lista = []
    for i in range(n):
        lista.append(i)
    return lista

def ad_a(n):
    lista = lista(n)
    return r.shuffle(lista)

def ad_b(n):
    lista = lista(n)
    el = lista[0]
    lista.pop(0)
    lista.append(el)
    return lista

def ad_c(n):
    lista = []
    for i in range(n-1, 0, -1):
        lista.append(i)
    el = lista[0]
    lista.pop(0)
    lista.append(el)
    return lista

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

def ad_e(n):
    max = mysqrt(n)
    while n > 0:
        yield r.randint(0, max)
        n-=1

