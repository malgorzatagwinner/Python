#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def napis(line):
    line = line.split()
    line = [i.zfill(3) for i in line]
    " ".join(line)
    print(line)
    
        

if __name__ == '__main__':
    #testy
    napis('1 12 33 450 654 30 400')


