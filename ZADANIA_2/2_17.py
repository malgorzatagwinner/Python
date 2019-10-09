#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def zmiana(line):
    line = line.split()
    line.sort()
    
    print(line)
    line.sort(key = len)
    print(line)

if __name__ == '__main__':
    #testy
    zmiana('GvR byl najlepszym malarzem z linii wszystkich GvR')


