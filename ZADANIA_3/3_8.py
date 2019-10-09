#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys, random

def common(a, b):
    return list(set(a) & set(b))

def everything(a,b):
    return list(set(a+b))

def random_list():
    return [random.randint(0, 10) for _ in range(random.randint(1, 10))]

a = random_list()
b = random_list()
print(a)
print(b)
print()
print(common(a, b))
print(everything(a, b))
