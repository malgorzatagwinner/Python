#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def ciag(numbers):
    out = ''
    for i in numbers:
        out+=str(i)
    print(out)

if __name__ == '__main__':
    #testy
    arr = [1, 2, 3, 4, 5] 
    ciag(arr)

